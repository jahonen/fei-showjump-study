import { useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '@/hooks/useAuth';
import './SignInScreen.scss';

/**
 * Entry point for unauthenticated visitors.
 * Renders a Google Sign-In button and redirects to dashboard once signed in.
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
      <div className="sign-in-card">
        <h1 id="app-title">ShowJump Study</h1>
        <p className="sign-in-subtitle">FEI Jumping Rules study tool</p>
        <button
          type="button"
          className="sign-in-button"
          onClick={signInWithGoogle}
          aria-label="Sign in with Google"
        >
          Sign in with Google
        </button>
        <p className="privacy-link">
          By signing in, you agree to our{' '}
          <Link to="/privacy">Privacy Notice</Link>.
        </p>
      </div>
    </main>
  );
}
