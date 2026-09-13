import {
  collection,
  doc,
  getDoc,
  getDocs,
  query,
  setDoc,
  updateDoc,
  where,
  writeBatch,
  serverTimestamp,
  Timestamp,
  type QueryDocumentSnapshot,
} from 'firebase/firestore';
import { db } from '@/services/firebase';
import type { Language, UserProfile, Attempt, ItemFlag, LeaderboardEntry, Variant, ParentItem } from '@/types';

const toDate = (value: unknown): Date | null => {
  if (value instanceof Timestamp) return value.toDate();
  if (value instanceof Date) return value;
  return null;
};

export async function ensureUserProfile(
  uid: string,
  displayName: string,
  email: string
): Promise<UserProfile> {
  const ref = doc(db, 'users', uid);
  const snap = await getDoc(ref);
  const now = new Date();

  if (!snap.exists()) {
    const profile: Omit<UserProfile, 'createdAt' | 'lastActiveAt'> & {
      createdAt: ReturnType<typeof serverTimestamp>;
      lastActiveAt: ReturnType<typeof serverTimestamp>;
    } = {
      displayName,
      email,
      preferredLanguage: 'en',
      publicName: null,
      createdAt: serverTimestamp(),
      lastActiveAt: serverTimestamp(),
    };
    await setDoc(ref, profile);
    return {
      displayName,
      email,
      preferredLanguage: 'en',
      publicName: null,
      createdAt: now,
      lastActiveAt: now,
    };
  }

  await updateDoc(ref, { lastActiveAt: serverTimestamp() });
  return parseUserProfile(snap);
}

export function parseUserProfile(snap: QueryDocumentSnapshot): UserProfile {
  const data = snap.data();
  return {
    displayName: data.displayName ?? '',
    email: data.email ?? '',
    preferredLanguage: data.preferredLanguage ?? 'en',
    publicName: data.publicName ?? null,
    createdAt: toDate(data.createdAt) ?? new Date(),
    lastActiveAt: toDate(data.lastActiveAt) ?? new Date(),
  };
}

export async function updatePreferredLanguage(uid: string, lang: Language): Promise<void> {
  await updateDoc(doc(db, 'users', uid), { preferredLanguage: lang, lastActiveAt: serverTimestamp() });
}

export async function updatePublicName(uid: string, publicName: string): Promise<void> {
  await updateDoc(doc(db, 'users', uid), { publicName, lastActiveAt: serverTimestamp() });
}

export async function getVerifiedItems(lang: Language): Promise<ParentItem[]> {
  const itemsCol = collection(db, 'questionBank', lang, 'items');
  const q = query(itemsCol, where('status', '==', 'verified'));
  const snap = await getDocs(q);
  return snap.docs.map(parseParentItem);
}

export function parseParentItem(docSnap: QueryDocumentSnapshot): ParentItem {
  const data = docSnap.data();
  const variants = Array.isArray(data.variants)
    ? data.variants.map((v: unknown) => parseVariant(v))
    : [];
  return {
    id: docSnap.id,
    domain: data.domain ?? '',
    article: data.article ?? '',
    editionRef: data.editionRef ?? '',
    status: data.status ?? 'draft',
    variants,
  };
}

function parseVariant(data: unknown): Variant {
  const v = (data ?? {}) as Record<string, unknown>;
  return {
    id: String(v.id ?? ''),
    parentId: String(v.parentId ?? ''),
    type: (v.type as 'single-select' | 'multi-select') ?? 'single-select',
    stem: String(v.stem ?? ''),
    options: (v.options as Record<string, string>) ?? {},
    correct: Array.isArray(v.correct) ? v.correct.map(String) : [],
    explanation: String(v.explanation ?? ''),
    sourcePage: typeof v.sourcePage === 'number' ? v.sourcePage : 0,
  };
}

export async function recordAttempt(uid: string, attempt: Attempt): Promise<void> {
  const attemptsCol = collection(db, 'users', uid, 'attempts');
  const ref = doc(attemptsCol);
  await setDoc(ref, {
    ...attempt,
    startedAt: Timestamp.fromDate(attempt.startedAt),
    completedAt: Timestamp.fromDate(attempt.completedAt),
  });
}

export async function getActiveFlags(uid: string, lang: Language): Promise<ItemFlag[]> {
  const flagsCol = collection(db, 'users', uid, 'itemFlags');
  const q = query(flagsCol, where('lang', '==', lang), where('status', '==', 'active'));
  const snap = await getDocs(q);
  return snap.docs.map(parseItemFlag);
}

export function parseItemFlag(docSnap: QueryDocumentSnapshot): ItemFlag {
  const data = docSnap.data();
  return {
    id: docSnap.id,
    lang: data.lang ?? 'en',
    domain: data.domain ?? '',
    firstMissedAt: toDate(data.firstMissedAt) ?? new Date(),
    lastAttemptAt: toDate(data.lastAttemptAt) ?? new Date(),
    consecutiveCorrect: data.consecutiveCorrect ?? 0,
    status: data.status ?? 'active',
    masteredAt: toDate(data.masteredAt),
  };
}

export async function updateItemFlag(
  uid: string,
  parentId: string,
  patch: Partial<ItemFlag>
): Promise<void> {
  const ref = doc(db, 'users', uid, 'itemFlags', parentId);
  await setDoc(
    ref,
    {
      ...patch,
      lastAttemptAt: serverTimestamp(),
      masteredAt: patch.masteredAt ? Timestamp.fromDate(patch.masteredAt) : null,
      firstMissedAt: patch.firstMissedAt ? Timestamp.fromDate(patch.firstMissedAt) : serverTimestamp(),
    },
    { merge: true }
  );
}

export async function logReviewEvent(
  uid: string,
  parentId: string,
  correct: boolean
): Promise<void> {
  const eventsCol = collection(db, 'users', uid, 'reviewHistory', parentId, 'events');
  await setDoc(doc(eventsCol), {
    answeredAt: serverTimestamp(),
    correct,
  });
}

export async function getLastReviewEvent(uid: string, parentId: string): Promise<{ answeredAt: Date; correct: boolean } | null> {
  const eventsCol = collection(db, 'users', uid, 'reviewHistory', parentId, 'events');
  const snap = await getDocs(eventsCol);
  if (snap.empty) return null;
  let latest: { answeredAt: Date; correct: boolean } | null = null;
  snap.docs.forEach((d) => {
    const date = toDate(d.data().answeredAt);
    if (date && (!latest || date > latest.answeredAt)) {
      latest = { answeredAt: date, correct: d.data().correct ?? false };
    }
  });
  return latest;
}

export async function getLeaderboard(lang: Language): Promise<LeaderboardEntry[]> {
  const snap = await getDocs(collection(db, 'leaderboard', lang, 'entries'));
  return snap.docs
    .map((d) => ({
      publicName: d.data().publicName ?? '',
      score: d.data().score ?? 0,
      questionsAnswered: d.data().questionsAnswered ?? 0,
      achievedAt: toDate(d.data().achievedAt) ?? new Date(),
    }))
    .sort((a, b) => b.score - a.score);
}

export async function getPersonalBest(uid: string, lang: Language): Promise<LeaderboardEntry | null> {
  const ref = doc(db, 'leaderboard', lang, 'entries', uid);
  const snap = await getDoc(ref);
  if (!snap.exists()) return null;
  const data = snap.data();
  return {
    publicName: data.publicName ?? '',
    score: data.score ?? 0,
    questionsAnswered: data.questionsAnswered ?? 0,
    achievedAt: toDate(data.achievedAt) ?? new Date(),
  };
}

export async function submitLeaderboardEntry(
  uid: string,
  lang: Language,
  entry: LeaderboardEntry
): Promise<void> {
  const ref = doc(db, 'leaderboard', lang, 'entries', uid);
  const existing = await getDoc(ref);
  if (existing.exists() && (existing.data().score ?? 0) >= entry.score) {
    return;
  }
  await setDoc(ref, {
    ...entry,
    achievedAt: Timestamp.fromDate(entry.achievedAt),
  });
}

export { writeBatch };
