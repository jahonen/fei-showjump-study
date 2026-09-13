import { useCallback, useEffect, useRef, useState } from 'react';
import type { ActiveQuestion, DomainBreakdown } from '@/types';

interface SessionState {
  questions: ActiveQuestion[];
  currentIndex: number;
  answers: Map<string, string[]>;
  results: Map<string, boolean>;
}

interface UseStudySessionReturn extends SessionState {
  answerQuestion: (variantId: string, selected: string[]) => void;
  nextQuestion: () => void;
  finish: () => {
    total: number;
    correct: number;
    breakdown: DomainBreakdown;
  };
}

export function useStudySession(initialQuestions: ActiveQuestion[]): UseStudySessionReturn {
  const [state, setState] = useState<SessionState>({
    questions: initialQuestions,
    currentIndex: 0,
    answers: new Map(),
    results: new Map(),
  });

  // Sync questions when they finish loading from Firestore. A ref is used to
  // detect real reference changes while tolerating parents that pass a new
  // array literal on every render.
  const syncedInitialRef = useRef(initialQuestions);
  useEffect(() => {
    if (syncedInitialRef.current === initialQuestions) return;
    syncedInitialRef.current = initialQuestions;

    setState((prev) => {
      const alreadyLoaded =
        initialQuestions.length === prev.questions.length && prev.questions.length > 0;
      if (alreadyLoaded) return prev;
      return {
        questions: initialQuestions,
        currentIndex: 0,
        answers: new Map(),
        results: new Map(),
      };
    });
  }, [initialQuestions]);

  const answerQuestion = useCallback((variantId: string, selected: string[]) => {
    const question = state.questions.find((q) => q.variant.id === variantId);
    if (!question) return;

    const sortedSelected = [...selected].sort();
    const sortedCorrect = [...question.variant.correct].sort();
    const isCorrect =
      sortedSelected.length === sortedCorrect.length &&
      sortedSelected.every((value, index) => value === sortedCorrect[index]);

    setState((prev) => {
      const answers = new Map(prev.answers);
      const results = new Map(prev.results);
      answers.set(variantId, selected);
      results.set(variantId, isCorrect);
      return { ...prev, answers, results };
    });
  }, [state.questions]);

  const nextQuestion = useCallback(() => {
    setState((prev) => ({
      ...prev,
      currentIndex: Math.min(prev.currentIndex + 1, prev.questions.length - 1),
    }));
  }, []);

  const finish = useCallback(() => {
    const breakdown: DomainBreakdown = {};
    let correct = 0;

    for (const question of state.questions) {
      const domain = question.parent.domain;
      if (!breakdown[domain]) {
        breakdown[domain] = { correct: 0, total: 0 };
      }
      breakdown[domain].total += 1;
      if (state.results.get(question.variant.id)) {
        correct += 1;
        breakdown[domain].correct += 1;
      }
    }

    return { total: state.questions.length, correct, breakdown };
  }, [state.questions, state.results]);

  return {
    ...state,
    answerQuestion,
    nextQuestion,
    finish,
  };
}
