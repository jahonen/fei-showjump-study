export type Language = 'en' | 'el' | 'fi';

export type QuestionType = 'single-select' | 'multi-select';

export type StudyMode = 'free-study' | 'timed-trial' | 'review' | 'highscore';

export interface Variant {
  id: string;
  parentId: string;
  type: QuestionType;
  stem: string;
  options: Record<string, string>;
  correct: string[];
  explanation: string;
  sourcePage: number;
}

export interface ParentItem {
  id: string;
  domain: string;
  article: string;
  editionRef: string;
  status: 'draft' | 'verified' | 'needs-revision';
  variants: Variant[];
}

export interface ActiveQuestion {
  variant: Variant;
  parent: ParentItem;
}

export interface UserProfile {
  displayName: string;
  email: string;
  preferredLanguage: Language;
  publicName: string | null;
  createdAt: Date;
  lastActiveAt: Date;
}

export interface Attempt {
  mode: 'free-study' | 'timed-trial';
  lang: Language;
  domainsIncluded: string[];
  startedAt: Date;
  completedAt: Date;
  totalQuestions: number;
  correctCount: number;
  domainBreakdown: Record<string, { correct: number; total: number }>;
}

export interface ItemFlag {
  id: string;
  lang: Language;
  domain: string;
  firstMissedAt: Date;
  lastAttemptAt: Date;
  consecutiveCorrect: number;
  status: 'active' | 'mastered';
  masteredAt: Date | null;
}

export interface LeaderboardEntry {
  publicName: string;
  score: number;
  questionsAnswered: number;
  achievedAt: Date;
}

export type DomainBreakdown = Record<string, { correct: number; total: number }>;
