# Integration documentation

## Firebase project

The app uses Firebase for authentication, database, and static hosting.

| Service | Product | Purpose |
|---|---|---|
| Auth | Firebase Authentication | Google Sign-In only |
| Database | Firestore | User profiles, attempts, flags, leaderboard, question bank |
| Hosting | Firebase Hosting | Static SPA deployment |

## Region configuration

All backend resources are configured for Europe:

- Firestore default database: `eur3` (multi-region Europe) — verify with `firebase firestore:databases:list --project=showjump-study --json`
- Cloud Functions (if added): deploy to `europe-west1` via `firebase.json` or per-function `region` option
- Hosting uses the Firebase global CDN edge network

## Environment variables

Client variables (Vite) are prefixed with `VITE_`. Server/ingestion variables are not.

See `.env.example` for the full list.

## Security rules

Firestore security rules are in `rules/firestore.rules`. Highlights:

- Users can only read/write their own `users/{uid}` subcollections.
- Question bank is read-only and filtered to `status == "verified"` (open to guests and signed-in users).
- Leaderboard is readable by any authenticated user and writable only by the entry owner, only if the new score is higher.

Deploy with `firebase deploy --only firestore:rules`.

## Privacy / GDPR

- Data controller: CVPE Development Ltd, Finnish business ID 3651473-2.
- Data privacy contact: <a href="mailto:dpo@cvpe.dev">dpo@cvpe.dev</a>.
- The Privacy Notice lives in the app at `/privacy` (`src/components/PrivacyNotice/`).
- Personal data is stored in Firestore in the European multi-region (`eur3`). Firebase Authentication and other Google Cloud subprocessors may process limited data outside the EEA under EU adequacy decisions and/or Standard Contractual Clauses.

## Question bank ingestion

Two ingestion options are available:

1. **Via gcloud REST API** (recommended when service-account keys are blocked by org policy):
   ```bash
   node app/functions/ingest-via-rest.mjs en
   ```
   This uses your authenticated gcloud account and the Firestore REST API to write verified parent items with inline variants.

2. **Via service-account key** (if key creation is allowed):
   ```bash
   cd app
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json npm run ingest en
   ```

Run either after any question-bank update.

## Third-party dependencies

| Dependency | Version | Purpose |
|---|---|---|
| firebase | ^10.13.0 | Firebase client SDK |
| firebase-admin | ^12.4.0 | Firestore ingestion script |
| react | ^18.3.1 | UI framework |
| react-dom | ^18.3.1 | DOM renderer |
| react-router-dom | ^6.26.0 | Client-side routing |
| vite | ^5.3.5 | Build tool |
| vitest | ^2.0.5 | Test runner |
| sass | ^1.77.8 | SCSS support |
| vite-plugin-pwa | ^0.20.1 | PWA manifest/service worker |
