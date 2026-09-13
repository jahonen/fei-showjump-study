import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { getVerifiedItems } from '@/services/firestore';
import ExitButton from '@/components/ExitButton/ExitButton';
import { formatDomainLabel } from '@/utils/questionSelection';
import type { Language, ParentItem } from '@/types';
import './FreeStudySetup.scss';

export default function FreeStudySetup() {
  const navigate = useNavigate();
  const location = useLocation();
  const [items, setItems] = useState<ParentItem[]>([]);
  const [selectedDomains, setSelectedDomains] = useState<Set<string>>(new Set());
  const [lang] = useState<Language>((location.state as { lang?: Language } | null)?.lang ?? 'en');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let cancelled = false;

    async function load() {
      const verified = await getVerifiedItems(lang);
      if (cancelled) return;
      setItems(verified);
      setSelectedDomains(new Set(verified.map((item) => item.domain)));
      setLoading(false);
    }

    load();
    return () => { cancelled = true; };
  }, [lang]);

  const domains = Array.from(new Set(items.map((item) => item.domain))).sort();

  const toggleDomain = (domain: string) => {
    setSelectedDomains((prev) => {
      const next = new Set(prev);
      if (next.has(domain)) {
        next.delete(domain);
      } else {
        next.add(domain);
      }
      return next;
    });
  };

  const start = () => {
    navigate('/study', {
      state: {
        mode: 'free-study',
        lang,
        domains: Array.from(selectedDomains),
      },
    });
  };

  const langLabel = formatLanguageLabel(lang);

  if (loading) {
    return <div className="loading" role="status">Loading domains…</div>;
  }

  return (
    <main className="free-study-setup" role="main">
      <header className="setup-header">
        <h1>Free Study</h1>
        <ExitButton />
      </header>
      <p className="setup-subtitle">
        Language: {langLabel}. Choose the domains you want to practise.
      </p>

      <fieldset className="domain-fieldset">
        <legend>Domains</legend>
        <div className="domain-list">
          {domains.map((domain) => (
            <label key={domain} className="domain-option">
              <input
                type="checkbox"
                checked={selectedDomains.has(domain)}
                onChange={() => toggleDomain(domain)}
              />
              <span>{formatDomainLabel(domain)}</span>
            </label>
          ))}
        </div>
      </fieldset>

      <div className="setup-actions">
        <button type="button" onClick={() => navigate('/dashboard')} className="secondary">
          Back
        </button>
        <button type="button" onClick={start} disabled={selectedDomains.size === 0}>
          Start
        </button>
      </div>
    </main>
  );
}
