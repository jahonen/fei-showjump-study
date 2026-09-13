import { describe, expect, it } from 'vitest';
import { selectVariants, formatDomainLabel, formatLanguageLabel } from '@/utils/questionSelection';
import type { ParentItem, Variant } from '@/types';

function makeVariant(id: string, parentId: string): Variant {
  return {
    id,
    parentId,
    type: 'single-select',
    stem: `Stem ${id}`,
    options: { A: 'A', B: 'B', C: 'C', D: 'D' },
    correct: ['A'],
    explanation: 'Explanation',
    sourcePage: 1,
  };
}

function makeParent(id: string, domain: string, count: number): ParentItem {
  return {
    id,
    domain,
    article: '200.1',
    editionRef: '',
    status: 'verified',
    variants: Array.from({ length: count }, (_, i) => makeVariant(`${id}-v${i}`, id)),
  };
}

describe('selectVariants', () => {
  it('returns the requested number of variants', () => {
    const items = [makeParent('p1', 'arena-warmup', 4), makeParent('p2', 'obstacles', 4)];
    const result = selectVariants(items, 4);
    expect(result.length).toBe(4);
  });

  it('does not serve variants from the same parent back-to-back', () => {
    const items = [
      makeParent('p1', 'arena-warmup', 10),
      makeParent('p2', 'obstacles', 10),
    ];
    const result = selectVariants(items, 8);
    for (let i = 1; i < result.length; i++) {
      expect(result[i].parent.id).not.toBe(result[i - 1].parent.id);
    }
  });

  it('excludes recently served variants when possible', () => {
    const items = [makeParent('p1', 'arena-warmup', 4)];
    const recent = ['p1-v0', 'p1-v1'];
    const result = selectVariants(items, 2, recent);
    const ids = result.map((q) => q.variant.id);
    expect(ids).not.toContain('p1-v0');
    expect(ids).not.toContain('p1-v1');
  });
});

describe('formatDomainLabel', () => {
  it('capitalizes hyphenated domains', () => {
    expect(formatDomainLabel('arena-warmup')).toBe('Arena Warmup');
    expect(formatDomainLabel('fines-warnings-elimination-disqualification')).toBe(
      'Fines Warnings Elimination Disqualification'
    );
  });
});

describe('formatLanguageLabel', () => {
  it('returns the expected labels', () => {
    expect(formatLanguageLabel('en')).toBe('English');
    expect(formatLanguageLabel('el')).toBe('Ελληνικά');
    expect(formatLanguageLabel('fi')).toBe('Suomi');
  });
});
