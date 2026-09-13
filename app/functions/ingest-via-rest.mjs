import { readdir, readFile } from 'fs/promises';
import { resolve, join } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

/**
 * Ingest the plaintext question bank into Firestore using the REST API and
 * the user's gcloud access token. This avoids needing a service-account key.
 *
 * Usage: node app/functions/ingest-via-rest.mjs <lang>
 */

const __filename = fileURLToPath(import.meta.url);
const repoRoot = resolve(__filename, '..', '..', '..');
const projectId = 'showjump-study';

function getAccessToken() {
  return execSync('gcloud auth print-access-token', { encoding: 'utf-8' }).trim();
}

async function loadItems(lang) {
  const itemsDir = resolve(repoRoot, 'questions', lang, 'items');
  const files = await walkFiles(itemsDir);
  const parents = new Map();
  const variants = [];

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

function toFirestoreValue(value) {
  if (value === null || value === undefined) {
    return { nullValue: null };
  }
  if (typeof value === 'string') {
    return { stringValue: value };
  }
  if (typeof value === 'number') {
    if (Number.isInteger(value)) {
      return { integerValue: String(value) };
    }
    return { doubleValue: value };
  }
  if (typeof value === 'boolean') {
    return { booleanValue: value };
  }
  if (Array.isArray(value)) {
    return { arrayValue: { values: value.map(toFirestoreValue) } };
  }
  if (typeof value === 'object') {
    const fields = {};
    for (const [k, v] of Object.entries(value)) {
      fields[k] = toFirestoreValue(v);
    }
    return { mapValue: { fields } };
  }
  return { stringValue: String(value) };
}

function docToFields(doc) {
  const fields = {};
  for (const [key, value] of Object.entries(doc)) {
    if (key === 'id') continue; // document ID is the doc name
    fields[key] = toFirestoreValue(value);
  }
  return fields;
}

async function ingest(lang) {
  const token = getAccessToken();
  const items = await loadItems(lang);
  console.log(`Found ${items.length} verified parent items for ${lang}.`);

  const writes = items.map((item) => ({
    update: {
      name: `projects/${projectId}/databases/(default)/documents/questionBank/${lang}/items/${item.id}`,
      fields: docToFields(item),
    },
  }));

  const url = `https://firestore.googleapis.com/v1/projects/${projectId}/databases/(default)/documents:batchWrite`;
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ writes }),
  });

  const body = await res.json();
  if (!res.ok) {
    console.error('Firestore batchWrite failed:', res.status, JSON.stringify(body, null, 2));
    process.exit(1);
  }
  console.log(`Ingested ${writes.length} documents for ${lang}.`);
}

const lang = process.argv[2];
if (!lang) {
  console.error('Usage: node app/functions/ingest-via-rest.mjs <lang>');
  process.exit(1);
}

ingest(lang).catch((err) => {
  console.error(err);
  process.exit(1);
});
