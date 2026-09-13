import * as functions from 'firebase-functions/v2';
import * as admin from 'firebase-admin';
import { readFile, readdir } from 'fs/promises';
import { join } from 'path';

/**
 * All Cloud Functions are deployed to europe-west1 by default to keep
 * Google Cloud resources in Europe.
 */
const REGION = 'europe-west1';

admin.initializeApp();
const db = admin.firestore();

/**
 * Admin-triggered ingestion of the plaintext question bank into Firestore.
 *
 * Input event data: { lang: "en" }
 * Reads files from the packaged questions/<lang>/items directory tree.
 */
export const ingestQuestionBank = functions.https.onCall(
  {
    region: REGION,
    memory: '256MiB',
    timeoutSeconds: 300,
    invoker: 'private',
  },
  async (request) => {
    const lang = request.data?.lang as string;
    if (!lang) {
      throw new functions.https.HttpsError('invalid-argument', 'Missing lang');
    }

    const itemsDir = join(__dirname, '..', 'questions', lang, 'items');
    const files = await walkFiles(itemsDir);

    const parents = new Map<string, ParentDoc>();
    const variants: VariantDoc[] = [];

    for (const filePath of files) {
      const text = await readFile(filePath, 'utf-8');
      const item = parseItem(text);
      if (item.status !== 'verified') continue;
      if (item.id === item.parentId) {
        parents.set(item.id, item);
      } else {
        variants.push(item);
      }
    }

    for (const variant of variants) {
      const parent = parents.get(variant.parentId);
      if (!parent) {
        console.warn(`Parent not found for variant ${variant.id}`);
        continue;
      }
      parent.variants.push(variant);
    }

    const batch = db.batch();
    let written = 0;

    for (const item of parents.values()) {
      const parentRef = db.collection('questionBank').doc(lang).collection('items').doc(item.id);
      const { variants: itemVariants, ...parentData } = item;

      batch.set(parentRef, parentData);
      written += 1;

      for (const variant of itemVariants) {
        const variantRef = parentRef.collection('variants').doc(variant.id);
        batch.set(variantRef, {
          type: variant.type,
          stem: variant.stem,
          options: variant.options,
          correct: variant.correct,
          explanation: variant.explanation,
          sourcePage: variant.sourcePage,
        });
        written += 1;
      }
    }

    await batch.commit();
    console.log(`Ingested ${written} documents for ${lang}`);
    return { written, parents: parents.size };
  }
);

interface ParentDoc {
  id: string;
  parentId: string;
  domain: string;
  article: string;
  editionRef: string;
  status: string;
  type?: string;
  stem?: string;
  options?: Record<string, string>;
  correct?: string[];
  explanation?: string;
  sourcePage?: number;
  variants: VariantDoc[];
}

type VariantDoc = ParentDoc;

function parseItem(text: string): ParentDoc {
  const data: Record<string, string> = {};
  for (const line of text.split('\n')) {
    const idx = line.indexOf(':');
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    const value = line.slice(idx + 1).trim();
    data[key] = value;
  }

  const options: Record<string, string> = {};
  for (const key of ['A', 'B', 'C', 'D']) {
    if (data[`OPTION_${key}`]) {
      options[key] = data[`OPTION_${key}`];
    }
  }

  return {
    id: data.ID,
    parentId: data.PARENT_ID,
    domain: data.DOMAIN,
    article: data.ARTICLE,
    editionRef: data.EDITION_REF,
    status: data.STATUS || 'draft',
    type: data.TYPE,
    stem: data.STEM,
    options,
    correct: data.CORRECT?.split(',').map((s) => s.trim()).filter(Boolean) ?? [],
    explanation: data.EXPLANATION,
    sourcePage: parseInt(data.SOURCE_PAGE, 10) || 0,
    variants: [],
  };
}

async function walkFiles(dir: string): Promise<string[]> {
  const result: string[] = [];
  try {
    const entries = await readdir(dir, { withFileTypes: true });
    for (const entry of entries) {
      const path = join(dir, entry.name);
      if (entry.isDirectory()) {
        result.push(...(await walkFiles(path)));
      } else if (entry.name.endsWith('.txt')) {
        result.push(path);
      }
    }
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== 'ENOENT') throw err;
  }
  return result;
}
