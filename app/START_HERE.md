# Start here — ShowJump Study app

This is the client application for the ShowJump Study question bank.

## Project structure

```
app/
  public/               # PWA icons and manifest
  src/
    components/         # React components, co-located with SCSS
    contexts/             # React contexts (AuthContext)
    hooks/                # Shared hooks (useStudySession)
    services/             # Firebase setup + Firestore helpers
    styles/               # main.scss, _variables.scss
    utils/                # question selection helpers
    types.ts              # shared TypeScript types
  functions/              # Node ingestion script
  rules/                  # Firestore security rules
```

## Conventions

- Components live in `src/components/ComponentName/` with `ComponentName.tsx` and `ComponentName.scss`.
- All files and folders use kebab-case unless framework-specific (e.g. component folders are PascalCase).
- Functions use camelCase; async functions that fetch data are prefixed with `fetch`, `load`, or `get`.
- Styling uses `main.scss` for shared variables and component-specific SCSS files.
- Lifecycle tags: this app is currently `alpha`.

## Next steps

1. Add your Firebase config to `.env`.
2. Run `npm install && npm run dev`.
3. Ingest the question bank: `npm run ingest en`.
4. Deploy Firestore rules and Hosting.
