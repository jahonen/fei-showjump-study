import { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { ensureUserProfile, updatePreferredLanguage, updatePublicName } from '@/services/firestore';
import { formatLanguageLabel } from '@/utils/questionSelection';
import type { Language, UserProfile } from '@/types';
import './Settings.scss';

export default function Settings() {
  const { user, logout } = useAuth();
  const navigate = useNavigate();
  const [profile, setProfile] = useState<UserProfile | null>(null);
  const [publicName, setPublicName] = useState('');
  const [saved, setSaved] = useState(false);

  useEffect(() => {
    if (!user) return;
    ensureUserProfile(user.uid, user.displayName ?? '', user.email ?? '').then((p) => {
      setProfile(p);
      setPublicName(p.publicName ?? '');
    });
  }, [user]);

  const savePublicName = async () => {
    if (!user) return;
    await updatePublicName(user.uid, publicName.trim().slice(0, 20));
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  const changeLanguage = async (lang: Language) => {
    if (!user || !profile) return;
    await updatePreferredLanguage(user.uid, lang);
    setProfile({ ...profile, preferredLanguage: lang });
  };

  const handleLogout = async () => {
    await logout();
    navigate('/');
  };

  const languages: Language[] = ['en']; // extend when el/fi banks exist

  return (
    <main className="settings" role="main">
      <h1>Settings</h1>

      <section className="settings-section" aria-labelledby="account-heading">
        <h2 id="account-heading">Account</h2>
        <p>
          <strong>{profile?.displayName}</strong>
        </p>
        <p className="muted">{profile?.email}</p>
      </section>

      <section className="settings-section" aria-labelledby="language-heading">
        <h2 id="language-heading">Preferred language</h2>
        <div className="language-options">
          {languages.map((lang) => (
            <label key={lang} className="language-option">
              <input
                type="radio"
                name="preferredLanguage"
                checked={profile?.preferredLanguage === lang}
                onChange={() => changeLanguage(lang)}
              />
              <span>{formatLanguageLabel(lang)}</span>
            </label>
          ))}
        </div>
      </section>

      <section className="settings-section" aria-labelledby="leaderboard-name-heading">
        <h2 id="leaderboard-name-heading">Public leaderboard name</h2>
        <p className="muted">Shown on the Highscore leaderboard instead of your real name.</p>
        <input
          type="text"
          value={publicName}
          onChange={(e) => setPublicName(e.target.value)}
          maxLength={20}
          placeholder="Enter a display name"
          aria-label="Public leaderboard name"
        />
        <button type="button" onClick={savePublicName} disabled={publicName.trim().length === 0}>
          Save
        </button>
        {saved && <p className="save-confirm" role="status">Saved.</p>}
      </section>

      <section className="settings-actions">
        <button type="button" className="secondary" onClick={() => navigate('/dashboard')}>
          Back
        </button>
        <button type="button" className="danger" onClick={handleLogout}>
          Sign out
        </button>
      </section>

      <p className="settings-privacy-link">
        <Link to="/privacy">Privacy Notice</Link>
      </p>
    </main>
  );
}
