# ShowJump Study — Application

Mobile-first web app for studying the FEI Jumping Rules. Built with React, Vite, Firebase Auth, and Firestore.

## Quick start

1. `cd app`
2. `npm install`
3. Copy `.env.example` to `.env` and fill in your Firebase project credentials.
4. `npm run dev`

## Scripts

- `npm run dev` — local development server
- `npm run build` — production build (outputs to `../dist`)
- `npm run preview` — preview production build
- `npm run test` — run Vitest tests
- `npm run ingest en` — ingest the English question bank into Firestore (requires service-account key)

## Firebase setup

1. Create a Firebase project.
2. Enable Google Sign-In in Authentication.
3. Create a Firestore database in a European region (e.g. `eur3`) and deploy the rules in `rules/firestore.rules`.
4. Generate a service account key for ingestion and set `GOOGLE_APPLICATION_CREDENTIALS`.
5. Deploy Cloud Functions to `europe-west1` if you add server-side functions.

## Deployment

The project is configured for Firebase Hosting. After running `npm run build`, deploy with `firebase deploy` (requires the Firebase CLI and a `firebase.json` at repo root).
