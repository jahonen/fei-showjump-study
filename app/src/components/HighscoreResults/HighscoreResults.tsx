import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import ExitButton from '@/components/ExitButton/ExitButton';
import { getPersonalBest, submitLeaderboardEntry } from '@/services/firestore';
import type { Language } from '@/types';
import './HighscoreResults.scss';

interface ResultsState {
  score: number;
  questionsAnswered: number;
  reason: 'timeout' | 'wrong' | null;
}

export default function HighscoreResults() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();
  const { score, questionsAnswered, reason } = (location.state as ResultsState | undefined) ?? {
    score: 0,
    questionsAnswered: 0,
    reason: null,
  };

  const [best, setBest] = useState<number | null>(null);
  const [submitted, setSubmitted] = useState(false);
  const [publicName, setPublicName] = useState('');
  const lang: Language = 'en';

  useEffect(() => {
    if (!user) return;
    getPersonalBest(user.uid, lang).then((entry) => {
      setBest(entry?.score ?? null);
    });
  }, [user]);

  const isNewBest = best === null || score > best;

  const submit = async () => {
    if (!user || !publicName.trim()) return;
    await submitLeaderboardEntry(user.uid, lang, {
      publicName: publicName.trim().slice(0, 20),
      score,
      questionsAnswered,
      achievedAt: new Date(),
    });
    setSubmitted(true);
  };

  return (
    <main className="highscore-results" role="main">
      <header className="results-header">
        <h1>Highscore Results</h1>
        <ExitButton />
      </header>

      <section className="result-summary" aria-label="Score summary">
        <p className="final-score">{score}</p>
        <p>
          Questions survived: {questionsAnswered}
          {reason === 'timeout' && <span className="reason"> (time ran out)</span>}
          {reason === 'wrong' && <span className="reason"> (wrong answer)</span>}
        </p>
        {best !== null && <p>Your best: {Math.max(best, score)}</p>}
      </section>

      {isNewBest && !submitted && (
        <section className="leaderboard-submit" aria-labelledby="leaderboard-heading">
          <h2 id="leaderboard-heading">New personal best!</h2>
          <label htmlFor="public-name">Public leaderboard name (max 20 characters)</label>
          <input
            id="public-name"
            type="text"
            value={publicName}
            onChange={(e) => setPublicName(e.target.value)}
            maxLength={20}
            placeholder="Enter a display name"
          />
          <button type="button" onClick={submit} disabled={!publicName.trim()}>
            Submit to leaderboard
          </button>
        </section>
      )}

      {submitted && <p className="success" role="status">Leaderboard entry submitted.</p>}

      <div className="result-actions">
        <button type="button" onClick={() => navigate('/highscore')}>Play again</button>
        <button type="button" className="secondary" onClick={() => navigate('/leaderboard')}>
          View leaderboard
        </button>
        <button type="button" className="secondary" onClick={() => navigate('/dashboard')}>
          Dashboard
        </button>
      </div>
    </main>
  );
}
