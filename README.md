# ShowJump Study

FEI Jumping Rules study tool.

- `questions/` — plaintext source-traceable question bank (English verified; Greek/Finnish pending official sources)
- `app/` — React + Vite + Firebase SPA (Free Study, Timed Trial, Review, Highscore)
- `functions/` — Cloud Functions (2nd gen) for question-bank ingestion and integrity checks, deployed to `europe-west1`
- `assets/` — PWA icons and favicons

See `app/START_HERE.md` and `app/README.md` for development instructions.

## Deployment

```bash
cd app
npm install
npm run build
cd ../functions
npm install
npm run build
cd ..
firebase deploy
```

All backend resources are configured for Europe:

- Firestore: `eur3`
- Cloud Functions: `europe-west1`
