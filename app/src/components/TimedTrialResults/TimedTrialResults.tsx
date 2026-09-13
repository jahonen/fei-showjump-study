import { useLocation, useNavigate } from 'react-router-dom';
import ExitButton from '@/components/ExitButton/ExitButton';
import { formatDomainLabel } from '@/utils/questionSelection';
import type { DomainBreakdown } from '@/types';
import './TimedTrialResults.scss';

interface ResultsState {
  total: number;
  correct: number;
  breakdown: DomainBreakdown;
}

export default function TimedTrialResults() {
  const navigate = useNavigate();
  const location = useLocation();
  const result = (location.state as ResultsState | undefined) ?? { total: 0, correct: 0, breakdown: {} };
  const { total, correct, breakdown } = result;

  const weakestDomain = Object.entries(breakdown)
    .sort((a, b) => {
      const ratioA = a[1].total ? a[1].correct / a[1].total : 0;
      const ratioB = b[1].total ? b[1].correct / b[1].total : 0;
      return ratioA - ratioB;
    })
    .map(([domain]) => domain)[0];

  return (
    <main className="timed-results" role="main">
      <header className="results-header">
        <h1>Timed Trial Results</h1>
        <ExitButton />
      </header>

      <section className="score-summary" aria-label="Score summary">
        <p className="big-score">
          {correct} / {total}
        </p>
        <p>{total > 0 ? Math.round((correct / total) * 100) : 0}% correct</p>
      </section>

      <section className="domain-breakdown" aria-labelledby="breakdown-heading">
        <h2 id="breakdown-heading">Breakdown by domain</h2>
        <table>
          <thead>
            <tr>
              <th scope="col">Domain</th>
              <th scope="col">Correct</th>
              <th scope="col">Total</th>
              <th scope="col">%</th>
            </tr>
          </thead>
          <tbody>
            {Object.entries(breakdown)
              .sort((a, b) => {
                const ratioA = a[1].total ? a[1].correct / a[1].total : 0;
                const ratioB = b[1].total ? b[1].correct / b[1].total : 0;
                return ratioA - ratioB;
              })
              .map(([domain, stats]) => (
                <tr key={domain}>
                  <td>{formatDomainLabel(domain)}</td>
                  <td>{stats.correct}</td>
                  <td>{stats.total}</td>
                  <td>
                    {stats.total > 0 ? Math.round((stats.correct / stats.total) * 100) : 0}%
                  </td>
                </tr>
              ))}
          </tbody>
        </table>
      </section>

      <div className="result-actions">
        {weakestDomain && (
          <button
            type="button"
            onClick={() =>
              navigate('/study', {
                state: { mode: 'free-study', lang: 'en', domains: [weakestDomain] },
              })
            }
          >
            Drill weakest: {formatDomainLabel(weakestDomain)}
          </button>
        )}
        <button type="button" className="secondary" onClick={() => navigate('/dashboard')}>
          Back to dashboard
        </button>
      </div>
    </main>
  );
}
