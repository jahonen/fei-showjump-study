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
  const [selectedLang, setSelectedLang] = useState<Language>('en');
  const [reviewCount, setReviewCount] = useState<number>(0);
  const [highscore, setHighscore] = useState<number | null>(null);

  const isGuest = user === null;

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
      setSelectedLang(profile.preferredLanguage);
      setReviewCount(flags.length);
      setHighscore(best?.score ?? null);
    }

    load();
    return () => { cancelled = true; };
  }, [user]);

  const changeLanguage = (lang: Language) => {
    setSelectedLang(lang);
    if (profile) {
      setProfile({ ...profile, preferredLanguage: lang });
    }
  };

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };

  const availableLanguages: Language[] = ['en', 'el']; // extend when fi bank exists

  return (
    <main className="dashboard" role="main">
      <header className="dashboard-header">
        <h1>ShowJump Study</h1>
        {isGuest ? (
          <button type="button" onClick={() => navigate('/')} className="logout-button">
            Sign in
          </button>
        ) : (
          <button type="button" onClick={handleLogout} className="logout-button">
            Sign out
          </button>
        )}
      </header>

      {isGuest && (
        <section className="guest-banner" aria-label="Guest mode">
          <p>
            You are using the app as a guest. Free Study and Timed Trial are available.
            Sign in to save your progress and unlock Review and Highscore.
          </p>
        </section>
      )}

      <section className="language-bar" aria-label="Language selector">
        {availableLanguages.map((lang) => (
          <button
            key={lang}
            type="button"
            className={selectedLang === lang ? 'active' : ''}
            onClick={() => changeLanguage(lang)}
            aria-pressed={selectedLang === lang}
          >
            {formatLanguageLabel(lang)}
          </button>
        ))}
      </section>

      <section className="mode-grid" aria-label="Study modes">
        <ModeCard
          title="Free Study"
          description="Untimed practice by domain with instant feedback."
          onClick={() => navigate('/free-study', { state: { lang: selectedLang } })}
        />
        <ModeCard
          title="Timed Trial"
          description="50 questions, 60 minutes, results at the end."
          onClick={() => navigate('/study', { state: { mode: 'timed-trial', lang: selectedLang } })}
        />
        <ModeCard
          title="Review"
          description={isGuest ? 'Sign in to review missed questions' : `${reviewCount} item${reviewCount === 1 ? '' : 's'} to review`}
          onClick={() => navigate('/review')}
          badge={!isGuest && reviewCount > 0 ? reviewCount : undefined}
          disabled={isGuest}
        />
        <ModeCard
          title="Highscore"
          description={isGuest ? 'Sign in to compete on the leaderboard' : highscore !== null ? `Best: ${highscore}` : 'Speed survival mode'}
          onClick={() => navigate('/highscore')}
          disabled={isGuest}
        />
      </section>

      <button
        type="button"
        className="settings-link"
        onClick={() => navigate('/settings')}
        disabled={isGuest}
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
  disabled?: boolean;
}

function ModeCard({ title, description, onClick, badge, disabled }: ModeCardProps) {
  return (
    <button
      type="button"
      className={`mode-card ${disabled ? 'disabled' : ''}`}
      onClick={onClick}
      aria-label={title}
      disabled={disabled}
    >
      <h2>{title}</h2>
      <p>{description}</p>
      {badge !== undefined && <span className="mode-badge" aria-label={`${badge} waiting`}>{badge}</span>}
    </button>
  );
}
