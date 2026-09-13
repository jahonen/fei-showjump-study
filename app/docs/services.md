# Service documentation

## firestore.ts

**Purpose:** Client-side Firestore helpers for reading/writing user data and the question bank.

**Inputs:**
- User IDs, language codes, parent IDs, and typed data objects.

**Outputs:**
- User profiles, verified items, attempts, flags, review history, and leaderboard entries.

**Side effects:** Performs Firestore reads/writes; creates user profile on first sign-in.

**External dependencies:** Firebase Firestore SDK.

## firebase.ts

**Purpose:** Initializes the Firebase app, Auth, and Firestore instances from environment variables.

**Inputs:** `import.meta.env` values for Firebase config.

**Outputs:** `auth`, `db`, `googleProvider`.

**Side effects:** Throws if any required environment variable is missing.

## Cloud Functions (functions/src/index.ts)

**Purpose:** Deployable 2nd-gen Cloud Functions for ingestion and integrity checks, pinned to `europe-west1`.

**Functions:**
- `ingestQuestionBank`: admin `onCall` trigger that ingests the plaintext repo into Firestore.
- `integrityCheck`: scheduled nightly check for malformed verified items.

**Side effects:** Writes to Firestore via Admin SDK.

**Start/end/error logging:** logs document counts and integrity issues.

## ingest-question-bank.mjs

**Purpose:** Ingests the plaintext question bank into Firestore.

**Inputs:**
- CLI language argument (e.g. `en`).
- `GOOGLE_APPLICATION_CREDENTIALS` environment variable.
- Plaintext files under `../../questions/<lang>/items/`.

**Outputs:**
- Writes/updates `questionBank/{lang}/items/{parentId}` docs and `variants/{variantId}` subdocs.

**Side effects:**
- Uses `firebase-admin` to commit batched writes.
- Logs counts to stdout.

**Start/end/error logging:** logs start, document count, and completion; errors cause non-zero exit.

**External dependencies:** `firebase-admin`.

## useStudySession.ts

**Purpose:** Manages the state for a study session: current question, answers, and scoring.

**Inputs:** Array of `ActiveQuestion` objects.

**Outputs:**
- `currentIndex`, `answers`, `results`.
- `answerQuestion(variantId, selected)`
- `nextQuestion()`
- `finish()` returns `{ total, correct, breakdown }`.

**Side effects:** None — pure client-side state hook.
