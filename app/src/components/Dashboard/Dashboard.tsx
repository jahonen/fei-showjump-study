import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { ensureUserProfile, getActiveFlags, getPersonalBest } from '@/services/firestore';
import { formatLanguageLabel } from '@/utils/questionSelection';
import type { Language, UserProfile } from '@/types';
import './Dashboard.scss';

export default function Dashboard() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [reviewCount, setReviewCount] = useState<number>(0);
  const [highscore, setHighscore] = useState<number | null>(null);

  useEffect(() => {
    if (!user) return;
    const uid = user.uid;
    const displayName = user.displayName ?? '';
    const email = user.email ?? '';
    let cancelled = false;

    async function load() {
      const profile = await ensureUserProfile(uid, displayName, email);
      const flags = await getActiveFlags(uid, profile.preferredLanguage);
      const best = await getPersonalBest(uid, profile.preferredLanguage);

      if (cancelled) return;
      setProfile(profile);
      setReviewCount(flags.length);
      setHighscore(best?.score ?? null);
    }

    load();
    return () => { cancelled = true; };
  }, [user]);

  const changeLanguage = (lang: Language) => {
    if (profile) {
      setProfile({ ...profile, preferredLanguage: lang });
    }
  };

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };

  const availableLanguages: Language[] = ['en']; // extend when el/fi banks exist

  return (
    <main className="dashboard" role="main">
      <header className="dashboard-header">
        <h1>ShowJump Study</h1>
        <button type="button" onClick={handleLogout} className="logout-button">
          Sign out
        </button>
      </header>

      <section className="language-bar" aria-label="Language selector">
        {availableLanguages.map((lang) => (
          <button
            key={lang}
            type="button"
            className={profile?.preferredLanguage === lang ? 'active' : ''}
            onClick={() => changeLanguage(lang)}
            aria-pressed={profile?.preferredLanguage === lang}
          >
            {formatLanguageLabel(lang)}
          </button>
        ))}
      </section>

      <section className="mode-grid" aria-label="Study modes">
        <ModeCard
          title="Free Study"
          description="Untimed practice by domain with instant feedback."
          onClick={() => navigate('/free-study')}
        />
        <ModeCard
          title="Timed Trial"
          description="50 questions, 60 minutes, results at the end."
          onClick={() => navigate('/study', { state: { mode: 'timed-trial' } })}
        />
        <ModeCard
          title="Review"
          description={`${reviewCount} item${reviewCount === 1 ? '' : 's'} to review`}
          onClick={() => navigate('/review')}
          badge={reviewCount > 0 ? reviewCount : undefined}
        />
        <ModeCard
          title="Highscore"
          description={highscore !== null ? `Best: ${highscore}` : 'Speed survival mode'}
          onClick={() => navigate('/highscore')}
        />
      </section>

      <button
        type="button"
        className="settings-link"
        onClick={() => navigate('/settings')}
      >
        Settings
      </button>
    </main>
  );
}

interface ModeCardProps {
  title: string;
  description: string;
  onClick: () => void;
  badge?: number;
}

function ModeCard({ title, description, onClick, badge }: ModeCardProps) {
  return (
    <button type="button" className="mode-card" onClick={onClick} aria-label={title}>
      <h2>{title}</h2>
      <p>{description}</p>
      {badge !== undefined && <span className="mode-badge" aria-label={`${badge} waiting`}>{badge}</span>}
    </button>
  );
}
