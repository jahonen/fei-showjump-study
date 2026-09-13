import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import ExitButton from '@/components/ExitButton/ExitButton';
import { getLeaderboard } from '@/services/firestore';
import { formatLanguageLabel } from '@/utils/questionSelection';
import type { Language, LeaderboardEntry } from '@/types';
import './Leaderboard.scss';

export default function Leaderboard() {
  const navigate = useNavigate();
  const [lang, setLang] = useState<Language>('en');
  const [entries, setEntries] = useState<LeaderboardEntry[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;
    setLoading(true);
    getLeaderboard(lang).then((data) => {
      if (cancelled) return;
      setEntries(data);
      setLoading(false);
    });
    return () => { cancelled = true; };
  }, [lang]);

  const languages: Language[] = ['en', 'el', 'fi'];

  return (
    <main className="leaderboard" role="main">
      <header className="leaderboard-header">
        <h1>Leaderboard</h1>
        <ExitButton />
      </header>

      <section className="language-bar" aria-label="Leaderboard language">
        {languages.map((l) => (
          <button
            key={l}
            type="button"
            className={lang === l ? 'active' : ''}
            onClick={() => setLang(l)}
            aria-pressed={lang === l}
          >
            {formatLanguageLabel(l)}
          </button>
        ))}
      </section>

      {loading ? (
        <p className="loading">Loading leaderboard…</p>
      ) : entries.length === 0 ? (
        <p className="empty-board">No entries yet.</p>
      ) : (
        <ol className="leaderboard-list" aria-label={`${formatLanguageLabel(lang)} leaderboard`}>
          {entries.map((entry, index) => (
            <li key={index} className="leaderboard-row">
              <span className="rank">{index + 1}</span>
              <span className="name">{entry.publicName}</span>
              <span className="score">{entry.score}</span>
              <span className="date">{entry.achievedAt.toLocaleDateString()}</span>
            </li>
          ))}
        </ol>
      )}

      <button type="button" className="back-button" onClick={() => navigate('/dashboard')}>
        Back to dashboard
      </button>
    </main>
  );
}
