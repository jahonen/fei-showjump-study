import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import { getActiveFlags } from '@/services/firestore';
import { formatDomainLabel } from '@/utils/questionSelection';
import type { ItemFlag, Language } from '@/types';
import './ReviewQueue.scss';

const LONG_QUEUE_THRESHOLD = 30;

export default function ReviewQueue() {
  const { user } = useAuth();
  const navigate = useNavigate();
  const [flags, setFlags] = useState<ItemFlag[]>([]);
  const lang: Language = 'en';
  const [loading, setLoading] = useState(true);
  const [sortByOldest, setSortByOldest] = useState(false);

  useEffect(() => {
    if (!user) return;
    const uid = user.uid;
    let cancelled = false;

    async function load() {
      const activeFlags = await getActiveFlags(uid, lang);
      if (cancelled) return;
      setFlags(activeFlags);
      setLoading(false);
    }

    load();
    return () => { cancelled = true; };
  }, [user, lang]);

  const byDomain: Record<string, ItemFlag[]> = {};
  for (const flag of flags) {
    if (!byDomain[flag.domain]) byDomain[flag.domain] = [];
    byDomain[flag.domain].push(flag);
  }

  const sortedDomains = Object.keys(byDomain).sort((a, b) => {
    if (!sortByOldest) return a.localeCompare(b);
    const oldestA = Math.min(...byDomain[a].map((f) => f.firstMissedAt.getTime()));
    const oldestB = Math.min(...byDomain[b].map((f) => f.firstMissedAt.getTime()));
    return oldestA - oldestB;
  });

  const startReview = (domain?: string) => {
    navigate('/study', {
      state: {
        mode: 'review',
        lang,
        domains: domain ? [domain] : undefined,
      },
    });
  };

  if (loading) {
    return <div className="loading" role="status">Loading review queue…</div>;
  }

  return (
    <main className="review-queue" role="main">
      <h1>Review</h1>

      {flags.length === 0 ? (
        <p className="empty-queue">No items to review. Nice work!</p>
      ) : (
        <>
          <p className="queue-count">{flags.length} item{flags.length === 1 ? '' : 's'} to review</p>

          {flags.length >= LONG_QUEUE_THRESHOLD && (
            <div className="queue-nudge" role="status">
              Your review queue is getting long.{' '}
              <button type="button" className="inline-link" onClick={() => setSortByOldest((s) => !s)}>
                {sortByOldest ? 'Show alphabetical' : 'Prioritize oldest misses'}
              </button>
            </div>
          )}

          <div className="review-all-bar">
            <button type="button" onClick={() => startReview()}>
              Review all
            </button>
          </div>

          <section className="domain-groups" aria-label="Review items by domain">
            {sortedDomains.map((domain) => (
              <article key={domain} className="domain-group">
                <h2>
                  {formatDomainLabel(domain)}{' '}
                  <span className="domain-count">({byDomain[domain].length})</span>
                </h2>
                <button type="button" onClick={() => startReview(domain)}>
                  Review {byDomain[domain].length} item
                  {byDomain[domain].length === 1 ? '' : 's'}
                </button>
              </article>
            ))}
          </section>
        </>
      )}

      <button type="button" className="back-button" onClick={() => navigate('/dashboard')}>
        Back to dashboard
      </button>
    </main>
  );
}
