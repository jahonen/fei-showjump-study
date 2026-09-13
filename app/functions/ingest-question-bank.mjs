import { readdir, readFile } from 'fs/promises';
import { resolve, join } from 'path';
import { fileURLToPath } from 'url';
import { initializeApp, cert } from 'firebase-admin/app';
import { getFirestore } from 'firebase-admin/firestore';

/**
 * Ingestion script for the plaintext question bank.
 *
 * Inputs:
 *   - CLI argument: language code (e.g. "en")
 *   - Environment variable GOOGLE_APPLICATION_CREDENTIALS pointing to a service-account JSON
 *   - Plaintext item files under ../../questions/<lang>/items/<domain>/<id>.txt
 *
 * Outputs:
 *   - Writes/updates Firestore documents at questionBank/<lang>/items/<parentId>
 *   - Populates the variants subcollection from sibling variant files.
 */

const __filename = fileURLToPath(import.meta.url);
const repoRoot = resolve(__filename, '..', '..', '..');

async function loadItems(lang) {
  const itemsDir = resolve(repoRoot, 'questions', lang, 'items');
  const files = await walkFiles(itemsDir);
  const parents = new Map();
  const variants = [];

  for (const filePath of files) {
    const text = await readFile(filePath, 'utf-8');
    const item = parseItem(text);
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

  return Array.from(parents.values());
}

function parseItem(text) {
  const data = {};
  for (const line of text.split('\n')) {
    const idx = line.indexOf(':');
    if (idx === -1) continue;
    const key = line.slice(0, idx).trim();
    const value = line.slice(idx + 1).trim();
    data[key] = value;
  }

  const options = {};
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
    sourcePage: parseInt(data.SOURCE_PAGE, 10) || 0,
    type: data.TYPE,
    stem: data.STEM,
    options,
    correct: data.CORRECT?.split(',').map((s) => s.trim()).filter(Boolean) ?? [],
    explanation: data.EXPLANATION,
    status: data.STATUS || 'draft',
    variants: [],
  };
}

async function walkFiles(dir) {
  const result = [];
  try {
    const entries = await readdir(dir, { withFileTypes: true });
    for (const entry of entries) {
      const path = join(dir, entry.name);
      if (entry.isDirectory()) {
        result.push(...await walkFiles(path));
      } else if (entry.name.endsWith('.txt')) {
        result.push(path);
      }
    }
  } catch (err) {
    if (err.code !== 'ENOENT') throw err;
  }
  return result;
}

async function ingest(lang) {
  console.log(`Starting ingestion for language: ${lang}`);
  const app = initializeApp({ projectId: process.env.FIREBASE_PROJECT_ID });
  const db = getFirestore(app);

  const items = await loadItems(lang);
  console.log(`Found ${items.length} parent items with variants.`);

  const batch = db.batch();
  let written = 0;

  for (const item of items) {
    const parentRef = db.collection('questionBank').doc(lang).collection('items').doc(item.id);
    const { variants, ...parentData } = item;

    batch.set(parentRef, parentData);
    written += 1;

    for (const variant of variants) {
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
  console.log(`Ingested ${written} documents for ${lang}.`);
}

const lang = process.argv[2];
if (!lang) {
  console.error('Usage: node functions/ingest-question-bank.mjs <lang>');
  process.exit(1);
}

ingest(lang).catch((err) => {
  console.error(err);
  process.exit(1);
});
