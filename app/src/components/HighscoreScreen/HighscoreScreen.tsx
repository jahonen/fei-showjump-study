import { useEffect, useRef, useState, useCallback } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import ExitButton from '@/components/ExitButton/ExitButton';
import { getVerifiedItems } from '@/services/firestore';
import { pickSingleSelectVariants } from '@/utils/questionSelection';
import type { ActiveQuestion } from '@/types';
import './HighscoreScreen.scss';

const INITIAL_TIME = 60;
const TIME_FLOOR = 4;
const SHRINK_FACTOR = 0.95;

interface RunState {
  questions: ActiveQuestion[];
  currentIndex: number;
  score: number;
  timeAllowed: number;
  timeLeft: number;
  questionsAnswered: number;
  gameOver: boolean;
  reason: 'timeout' | 'wrong' | null;
}

export default function HighscoreScreen() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [run, setRun] = useState<RunState | null>(null);
  const [loading, setLoading] = useState(true);
  const runRef = useRef<RunState | null>(null);
  const currentRef = useRef<ActiveQuestion | null>(null);

  runRef.current = run;
  currentRef.current = run ? run.questions[run.currentIndex] : null;

  useEffect(() => {
    if (!user) return;
    let cancelled = false;

    async function load() {
      const items = await getVerifiedItems('en');
      const questions = pickSingleSelectVariants(items, Infinity);
      if (cancelled) return;
      setRun({
        questions,
        currentIndex: 0,
        score: 0,
        timeAllowed: INITIAL_TIME,
        timeLeft: INITIAL_TIME,
        questionsAnswered: 0,
        gameOver: false,
        reason: null,
      });
      setLoading(false);
    }

    load();
    return () => { cancelled = true; };
  }, [user]);

  const endRun = useCallback((reason: 'timeout' | 'wrong') => {
    setRun((prev) => {
      if (!prev || prev.gameOver) return prev;
      return { ...prev, gameOver: true, reason, timeLeft: 0 };
    });
  }, []);

  useEffect(() => {
    if (!run || run.gameOver) return;

    const start = performance.now();
    let animationFrame = 0;

    const tick = () => {
      const currentRun = runRef.current;
      if (!currentRun || currentRun.gameOver) return;

      const elapsed = (performance.now() - start) / 1000;
      const remaining = Math.max(currentRun.timeAllowed - elapsed, 0);

      setRun((prev) => (prev ? { ...prev, timeLeft: remaining } : prev));

      if (remaining <= 0) {
        endRun('timeout');
        return;
      }
      animationFrame = requestAnimationFrame(tick);
    };

    animationFrame = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(animationFrame);
    // Refs are used inside tick to avoid re-creating the loop on every render.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [endRun]);

  useEffect(() => {
    if (run?.gameOver) {
      navigate('/highscore-results', {
        state: { score: run.score, questionsAnswered: run.questionsAnswered, reason: run.reason },
      });
    }
  }, [run?.gameOver, run?.score, run?.questionsAnswered, run?.reason, navigate]);

  const answer = (key: string) => {
    const current = currentRef.current;
    if (!current) return;

    if (!current.variant.correct.includes(key)) {
      endRun('wrong');
      return;
    }

    const currentRun = runRef.current;
    if (!currentRun) return;

    const points = Math.round(100 - currentRun.timeAllowed);
    const nextTimeAllowed = Math.max(currentRun.timeAllowed * SHRINK_FACTOR, TIME_FLOOR);

    setRun((prev) => {
      if (!prev) return prev;
      return {
        ...prev,
        score: prev.score + points,
        currentIndex: prev.currentIndex + 1,
        questionsAnswered: prev.questionsAnswered + 1,
        timeAllowed: nextTimeAllowed,
        timeLeft: nextTimeAllowed,
      };
    });
  };

  if (loading) {
    return <div className="loading" role="status">Loading…</div>;
  }

  if (!run || !currentRef.current) {
    return (
      <main className="highscore-screen" role="main">
        <p>No questions available for Highscore mode.</p>
        <button type="button" onClick={() => navigate('/dashboard')}>Back</button>
      </main>
    );
  }

  const current = currentRef.current;

  return (
    <main className="highscore-screen" role="main">
      <header className="highscore-header" aria-live="assertive">
        <span className="highscore-score" aria-label={`Score ${run.score}`}>
          {run.score}
        </span>
        <div className="highscore-header-actions">
          <span
            className="highscore-timer"
            aria-label={`${Math.ceil(run.timeLeft)} seconds remaining`}
          >
            {Math.ceil(run.timeLeft)}s
          </span>
          <ExitButton />
        </div>
      </header>

      <section className="highscore-card" aria-labelledby="highscore-stem">
        <p id="highscore-stem" className="highscore-stem">
          {current.variant.stem}
        </p>
        <div className="highscore-options" role="group" aria-label="Answer options">
          {(['A', 'B', 'C', 'D'] as const).map((key) => (
            <button
              key={key}
              type="button"
              className="highscore-option"
              onClick={() => answer(key)}
              aria-label={`Option ${key}: ${current.variant.options[key]}`}
            >
              {current.variant.options[key]}
            </button>
          ))}
        </div>
      </section>
    </main>
  );
}
