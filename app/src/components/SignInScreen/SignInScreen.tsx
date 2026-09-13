import { useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import './SignInScreen.scss';

/**
 * Entry point for unauthenticated visitors.
 * Renders a Google Sign-In button, redirects authenticated users to the dashboard,
 * and displays SEO-friendly hero content for new riders learning FEI Jumping Rules.
 */
export default function SignInScreen() {
  const { user, signInWithGoogle } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    if (user) {
      navigate('/dashboard');
    }
  }, [user, navigate]);

  return (
    <main className="sign-in-screen" role="main" aria-labelledby="app-title">
      <article className="hero-content">
        <img
          src="/web-app-manifest-512x512.png"
          alt="ShowJump Study logo: a horse reading a rulebook"
          className="hero-logo"
          width="160"
          height="160"
        />
        <h1 id="app-title">ShowJump Study</h1>
        <p className="hero-tagline">
          Master the FEI Jumping Rules with a free study app built for riders, trainers, and
          officials.
        </p>

        <section aria-labelledby="modes-heading">
          <h2 id="modes-heading">How it works</h2>
          <ul className="feature-list">
            <li>
              <strong>Free Study</strong> — browse by domain with instant explanations and article
              references.
            </li>
            <li>
              <strong>Timed Trial</strong> — 50 questions in 60 minutes with a domain-by-domain
              breakdown.
            </li>
            <li>
              <strong>Review</strong> — revisit missed questions until you master them.
            </li>
            <li>
              <strong>Highscore</strong> — test your speed with a shrinking-timer survival mode.
            </li>
          </ul>
        </section>

        <section aria-labelledby="why-heading">
          <h2 id="why-heading">Why use it?</h2>
          <p>
            Every question is traced directly to the official FEI Jumping Rules PDF, with article
            numbers and exact source pages. New riders can build confidence quickly, and experienced
            riders can keep the rules fresh before competitions.
          </p>
        </section>
      </article>

      <div className="sign-in-card">
        <h2 className="sign-in-heading">Start studying</h2>
        <p className="sign-in-subtitle">Sign in with Google to save your progress.</p>
        <button
          type="button"
          className="sign-in-button"
          onClick={signInWithGoogle}
          aria-label="Sign in with Google"
        >
          Sign in with Google
        </button>
        <button
          type="button"
          className="guest-button"
          onClick={() => navigate('/dashboard')}
        >
          Continue without signing in
        </button>
        <p className="privacy-link">
          By using this app, you agree to our{' '}
          <Link to="/privacy">Privacy Notice</Link>.
        </p>
      </div>
    </main>
  );
}
