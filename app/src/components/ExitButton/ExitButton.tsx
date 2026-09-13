import { useNavigate } from 'react-router-dom';
import './ExitButton.scss';

interface ExitButtonProps {
  label?: string;
}

/**
 * Top-right exit button that returns the user to the dashboard.
 * Used across all study/game mode screens.
 */
export default function ExitButton({ label = 'Exit' }: ExitButtonProps) {
  const navigate = useNavigate();

  return (
    <button
      type="button"
      className="exit-button"
      onClick={() => navigate('/dashboard')}
      aria-label="Exit to dashboard"
    >
      {label}
    </button>
  );
}
