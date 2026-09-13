import { describe, expect, it, vi } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import ExitButton from '../ExitButton';

const mockNavigate = vi.fn();

vi.mock('react-router-dom', async () => {
  const actual = await vi.importActual('react-router-dom');
  return {
    ...actual,
    useNavigate: () => mockNavigate,
  };
});

describe('ExitButton', () => {
  it('navigates to dashboard when clicked', () => {
    render(
      <MemoryRouter>
        <ExitButton />
      </MemoryRouter>
    );

    fireEvent.click(screen.getByRole('button', { name: /exit to dashboard/i }));
    expect(mockNavigate).toHaveBeenCalledWith('/dashboard');
  });

  it('renders custom label when provided', () => {
    render(
      <MemoryRouter>
        <ExitButton label="Quit" />
      </MemoryRouter>
    );

    expect(screen.getByText('Quit')).toBeInTheDocument();
  });
});
