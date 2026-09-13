import { describe, expect, it } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useStudySession } from '@/hooks/useStudySession';
import type { ActiveQuestion } from '@/types';

function makeQuestion(id: string, correct: string[], type: 'single-select' | 'multi-select' = 'single-select'): ActiveQuestion {
  return {
    parent: {
      id: id.includes('-') ? id.split('-')[0] : id,
      domain: 'arena-warmup',
      article: '200.1',
      editionRef: '',
      status: 'verified',
      variants: [],
    },
    variant: {
      id,
      parentId: id.includes('-') ? id.split('-')[0] : id,
      type,
      stem: 'Stem',
      options: { A: 'A', B: 'B', C: 'C', D: 'D' },
      correct,
      explanation: 'Explanation',
      sourcePage: 1,
    },
  };
}

describe('useStudySession', () => {
  it('tracks correct answers for single-select', () => {
    const { result } = renderHook(() => useStudySession([makeQuestion('q1', ['B'])]));
    act(() => result.current.answerQuestion('q1', ['B']));
    expect(result.current.results.get('q1')).toBe(true);
  });

  it('marks incorrect answers for single-select', () => {
    const { result } = renderHook(() => useStudySession([makeQuestion('q1', ['B'])]));
    act(() => result.current.answerQuestion('q1', ['A']));
    expect(result.current.results.get('q1')).toBe(false);
  });

  it('requires all correct options for multi-select', () => {
    const { result } = renderHook(() =>
      useStudySession([makeQuestion('q1', ['A', 'C'], 'multi-select')])
    );
    act(() => result.current.answerQuestion('q1', ['A', 'C']));
    expect(result.current.results.get('q1')).toBe(true);

    const { result: result2 } = renderHook(() =>
      useStudySession([makeQuestion('q1', ['A', 'C'], 'multi-select')])
    );
    act(() => result2.current.answerQuestion('q1', ['A']));
    expect(result2.current.results.get('q1')).toBe(false);
  });

  it('advances to the next question', () => {
    const { result } = renderHook(() =>
      useStudySession([makeQuestion('q1', ['A']), makeQuestion('q2', ['B'])])
    );
    expect(result.current.currentIndex).toBe(0);
    act(() => result.current.nextQuestion());
    expect(result.current.currentIndex).toBe(1);
  });

  it('computes finish results with domain breakdown', () => {
    const q1 = makeQuestion('q1', ['A']);
    const q2 = makeQuestion('q2', ['B']);
    const { result } = renderHook(() => useStudySession([q1, q2]));
    act(() => {
      result.current.answerQuestion('q1', ['A']);
      result.current.nextQuestion();
      result.current.answerQuestion('q2', ['A']);
    });
    const summary = result.current.finish();
    expect(summary.total).toBe(2);
    expect(summary.correct).toBe(1);
    expect(summary.breakdown['arena-warmup']).toEqual({ correct: 1, total: 2 });
  });
});
