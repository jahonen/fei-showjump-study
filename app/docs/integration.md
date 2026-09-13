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
- Question bank is read-only for authenticated users and filtered to `status == "verified"`.
- Leaderboard is readable by any authenticated user and writable only by the entry owner, only if the new score is higher.

Deploy with `firebase deploy --only firestore:rules`.

## Question bank ingestion

Run after any question-bank update:

```bash
npm run ingest en
```

This uses a service-account key with Firestore write access.

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
