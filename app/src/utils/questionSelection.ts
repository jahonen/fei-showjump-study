import type { ParentItem, ActiveQuestion, Language } from '@/types';

/**
 * Returns a random set of variants while avoiding:
 *  - variants from the same parent appearing back-to-back in the sequence
 *  - variants present in the user's recent history (last 20)
 */
export function selectVariants(
  items: ParentItem[],
  count: number,
  recentVariantIds: string[] = []
): ActiveQuestion[] {
  const allVariants = items.flatMap((parent) =>
    parent.variants.map((variant) => ({ variant, parent }))
  );

  const eligible = allVariants.filter(
    ({ variant }) => !recentVariantIds.includes(variant.id)
  );

  const sourcePool = eligible.length > 0 ? eligible : allVariants;
  const singleParent = new Set(sourcePool.map((q) => q.parent.id)).size <= 1;

  const shuffled = shuffle(sourcePool);
  const result: ActiveQuestion[] = [];
  const deferred: ActiveQuestion[] = [];

  for (const candidate of shuffled) {
    const last = result[result.length - 1];
    if (!singleParent && last && last.parent.id === candidate.parent.id) {
      deferred.push(candidate);
      continue;
    }
    result.push(candidate);
    if (result.length === count) break;
  }

  // Try deferred candidates after a different parent has been placed.
  for (const candidate of shuffle(deferred)) {
    if (result.length >= count) break;
    const last = result[result.length - 1];
    if (!singleParent && last && last.parent.id === candidate.parent.id) continue;
    result.push(candidate);
  }

  if (result.length < count) {
    const usedIds = new Set(result.map((r) => r.variant.id));
    const fallback = shuffle(sourcePool).filter((v) => !usedIds.has(v.variant.id));
    result.push(...fallback.slice(0, count - result.length));
  }

  return result;
}

function shuffle<T>(array: T[]): T[] {
  const copy = [...array];
  for (let i = copy.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [copy[i], copy[j]] = [copy[j], copy[i]];
  }
  return copy;
}

export function pickSingleSelectVariants(items: ParentItem[], count: number): ActiveQuestion[] {
  const singleSelectItems = items.map((parent) => ({
    ...parent,
    variants: parent.variants.filter((v) => v.type === 'single-select'),
  }));
  return selectVariants(singleSelectItems, count);
}

export function formatDomainLabel(domain: string): string {
  return domain
    .split('-')
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}

export function formatLanguageLabel(lang: Language): string {
  const labels: Record<Language, string> = {
    en: 'English',
    el: 'Ελληνικά',
    fi: 'Suomi',
  };
  return labels[lang];
}
