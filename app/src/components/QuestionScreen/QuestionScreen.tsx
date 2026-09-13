import { useEffect, useRef, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import {
  getActiveFlags,
  getLastReviewEvent,
  getVerifiedItems,
  logReviewEvent,
  recordAttempt,
  updateItemFlag,
} from '@/services/firestore';
import { useStudySession } from '@/hooks/useStudySession';
import { selectVariants, formatDomainLabel } from '@/utils/questionSelection';
import type { ActiveQuestion, ItemFlag, Language } from '@/types';
import './QuestionScreen.scss';

interface LocationState {
  mode: 'free-study' | 'timed-trial' | 'review';
  lang?: Language;
  domains?: string[];
}

const TIMED_TRIAL_MINUTES = 60;
const REVIEW_GAP_HOURS = 1;

export default function QuestionScreen() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const state = (location.state as LocationState | undefined) ?? { mode: 'free-study' };
  const mode = state.mode;

  const [questions, setQuestions] = useState<ActiveQuestion[]>([]);
  const [flags, setFlags] = useState<Record<string, ItemFlag>>({});
  const [loading, setLoading] = useState(true);
  const [startedAt] = useState<Date>(new Date());

  const session = useStudySession(questions);
  const current = questions[session.currentIndex];

  const [selected, setSelected] = useState<string[]>([]);
  const [submitted, setSubmitted] = useState(false);
  const [timeLeft, setTimeLeft] = useState<number>(TIMED_TRIAL_MINUTES * 60);
  const timeExpiredRef = useRef(false);
  const finishRef = useRef<() => void>(() => {});

  // Load questions
  useEffect(() => {
    if (!user) return;
    const uid = user.uid;
    let cancelled = false;

    async function load() {
      const lang = state.lang ?? 'en';
      const allItems = await getVerifiedItems(lang);

      let selectedQuestions: ActiveQuestion[] = [];
      if (mode === 'review') {
        const activeFlags = await getActiveFlags(uid, lang);
        const parentIds = new Set(activeFlags.map((f) => f.id));
        const reviewItems = allItems.filter((item) => parentIds.has(item.id));
        selectedQuestions = selectVariants(reviewItems, activeFlags.length);
        const flagMap: Record<string, ItemFlag> = {};
        activeFlags.forEach((flag) => {
          flagMap[flag.id] = flag;
        });
        setFlags(flagMap);
      } else if (mode === 'timed-trial') {
        selectedQuestions = selectVariants(allItems, 50);
      } else {
        const domains = state.domains ?? allItems.map((i) => i.domain);
        const filtered = allItems.filter((item) => domains.includes(item.domain));
        selectedQuestions = selectVariants(filtered, 20);
      }

      if (!cancelled) {
        setQuestions(selectedQuestions);
        setLoading(false);
      }
    }

    load();
    return () => { cancelled = true; };
  }, [user, mode, state.lang, state.domains]);

  // Timed trial countdown
  useEffect(() => {
    if (mode !== 'timed-trial' || loading || questions.length === 0) return;
    timeExpiredRef.current = false;
    const interval = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1 && !timeExpiredRef.current) {
          timeExpiredRef.current = true;
          finishRef.current();
          return 0;
        }
        return prev <= 1 ? prev : prev - 1;
      });
    }, 1000);
    return () => clearInterval(interval);
  }, [mode, loading, questions.length]);

  const handleFinish = async () => {
    if (!user) return;
    const uid = user.uid;
    const result = session.finish();

    if (mode === 'free-study' || mode === 'timed-trial') {
      await recordAttempt(uid, {
        mode,
        lang: (state.lang ?? 'en') as Language,
        domainsIncluded: state.domains ?? [],
        startedAt,
        completedAt: new Date(),
        totalQuestions: result.total,
        correctCount: result.correct,
        domainBreakdown: result.breakdown,
      });
    }

    if (mode === 'timed-trial') {
      navigate('/timed-results', { state: { ...result, mode } });
    } else {
      navigate('/dashboard');
    }
  };

  finishRef.current = handleFinish;

  const handleSubmit = async () => {
    if (!current || selected.length === 0 || !user) return;
    const uid = user.uid;

    session.answerQuestion(current.variant.id, selected);

    if (mode === 'free-study' || mode === 'review') {
      setSubmitted(true);

      if (mode === 'review') {
        const parentId = current.parent.id;
        const flag = flags[parentId];
        const isCorrect =
          current.variant.correct.length === selected.length &&
          current.variant.correct.every((c) => selected.includes(c));

        if (flag && isCorrect) {
          const lastEvent = await getLastReviewEvent(uid, parentId);
          const now = new Date();
          const canIncrement =
            !lastEvent ||
            (now.getTime() - lastEvent.answeredAt.getTime()) / 36e5 >= REVIEW_GAP_HOURS;

          if (canIncrement && flag.consecutiveCorrect + 1 >= 2) {
            await updateItemFlag(uid, parentId, {
              ...flag,
              consecutiveCorrect: flag.consecutiveCorrect + 1,
              status: 'mastered',
              masteredAt: now,
            });
          } else if (canIncrement) {
            await updateItemFlag(uid, parentId, {
              ...flag,
              consecutiveCorrect: flag.consecutiveCorrect + 1,
            });
          }
        } else if (flag && !isCorrect) {
          await updateItemFlag(uid, parentId, {
            ...flag,
            consecutiveCorrect: 0,
            status: 'active',
          });
        }
        await logReviewEvent(uid, parentId, isCorrect);
      }
    } else if (mode === 'timed-trial') {
      if (session.currentIndex === questions.length - 1) {
        await handleFinish();
      } else {
        advance();
      }
    }
  };

  const advance = () => {
    session.nextQuestion();
    setSelected([]);
    setSubmitted(false);
  };

  const toggleOption = (key: string) => {
    if (submitted) return;
    if (current?.variant.type === 'single-select') {
      setSelected([key]);
    } else {
      setSelected((prev) =>
        prev.includes(key) ? prev.filter((k) => k !== key) : [...prev, key]
      );
    }
  };

  if (loading) {
    return <div className="loading" role="status">Loading questions…</div>;
  }

  if (questions.length === 0) {
    return (
      <main className="question-screen" role="main">
        <p>No questions available.</p>
        <button type="button" onClick={() => navigate('/dashboard')}>Back</button>
      </main>
    );
  }

  if (!current) {
    return (
      <main className="question-screen" role="main">
        <p>Session complete.</p>
        <button type="button" onClick={handleFinish}>Finish</button>
      </main>
    );
  }

  const isCorrect =
    current.variant.correct.length === selected.length &&
    current.variant.correct.every((c) => selected.includes(c));

  const progressText = `${session.currentIndex + 1} / ${questions.length}`;
  const timerText =
    mode === 'timed-trial'
      ? `${Math.floor(timeLeft / 60)}:${String(timeLeft % 60).padStart(2, '0')}`
      : null;

  return (
    <main className="question-screen" role="main">
      <header
        className="question-header"
        aria-live={mode === 'timed-trial' ? 'polite' : undefined}
      >
        <span className="progress">{progressText}</span>
        {timerText && (
          <span className="timer" aria-label={`${timeLeft} seconds remaining`}>
            {timerText}
          </span>
        )}
      </header>

      <section className="question-card" aria-labelledby="question-stem">
        <p id="question-stem" className="stem">
          {current.variant.stem}
        </p>
        <p className="meta">
          {formatDomainLabel(current.parent.domain)} · {current.parent.article} · p.{' '}
          {current.variant.sourcePage}
        </p>

        <fieldset className="options-fieldset">
          <legend className="visually-hidden">Answer options</legend>
          {(['A', 'B', 'C', 'D'] as const).map((key) => (
            <button
              key={key}
              type="button"
              className={`option ${selected.includes(key) ? 'selected' : ''} ${
                submitted && current.variant.correct.includes(key) ? 'correct' : ''
              } ${
                submitted && selected.includes(key) && !current.variant.correct.includes(key)
                  ? 'incorrect'
                  : ''
              }`}
              onClick={() => toggleOption(key)}
              aria-pressed={selected.includes(key)}
              disabled={submitted}
              aria-label={`Option ${key}: ${current.variant.options[key]}`}
            >
              <span className="option-key">{key}</span>
              <span className="option-text">{current.variant.options[key]}</span>
            </button>
          ))}
        </fieldset>

        {mode !== 'timed-trial' && (
          <button
            type="button"
            className="submit-button"
            onClick={submitted ? advance : handleSubmit}
            disabled={!submitted && selected.length === 0}
          >
            {submitted ? 'Next' : 'Submit'}
          </button>
        )}

        {mode === 'timed-trial' && !submitted && (
          <button
            type="button"
            className="submit-button"
            onClick={handleSubmit}
            disabled={selected.length === 0}
          >
            Next
          </button>
        )}

        {submitted && mode !== 'timed-trial' && (
          <div className="feedback" role="status" aria-live="polite">
            <p className={isCorrect ? 'correct-label' : 'incorrect-label'}>
              {isCorrect ? 'Correct' : 'Incorrect'}
            </p>
            <p className="explanation">{current.variant.explanation}</p>
          </div>
        )}
      </section>
    </main>
  );
}
