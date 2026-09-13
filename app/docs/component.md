# Component documentation

## AuthContext

**Purpose:** Provides Firebase Authentication state and sign-in/out actions to the component tree.

**Inputs:**
- `children`: React nodes to render inside the provider.

**Outputs:**
- `user: User | null` — current Firebase user.
- `loading: boolean` — whether auth state is still being determined.
- `signInWithGoogle(): Promise<void>`
- `logout(): Promise<void>`

**Side effects:** Subscribes to `onAuthStateChanged` on mount.

**Location:** `src/contexts/AuthContext.tsx`

## Dashboard

**Purpose:** Entry screen after sign-in. Shows mode cards, language selector, and review queue count.

**Inputs:** None — reads from `AuthContext` and Firestore.

**Outputs:** Renders navigation to Free Study, Timed Trial, Review, Highscore, and Settings.

**Side effects:** Fetches user profile, active review flags, and personal best on mount.

**Analytics events:** `dashboard_view`, `mode_select`, `language_change`.

**Location:** `src/components/Dashboard/`

## FreeStudySetup

**Purpose:** Domain selection screen before a Free Study session.

**Inputs:** None — reads language from user profile.

**Outputs:** Navigates to `/study` with selected domains.

**Side effects:** Loads verified items to determine available domains.

**Location:** `src/components/FreeStudySetup/`

## QuestionScreen

**Purpose:** Shared question screen for Free Study, Timed Trial, and Review modes.

**Inputs (via location.state):**
- `mode: 'free-study' | 'timed-trial' | 'review'`
- `lang?: Language`
- `domains?: string[]`

**Outputs:** Records answers, updates review flags, and writes `attempts` documents.

**Side effects:**
- Loads randomized questions.
- Runs session-level 60-minute timer in Timed Trial.
- Updates `itemFlags` and `reviewHistory` in Review mode.

**Analytics events:** `question_answered`, `session_finished`.

**Location:** `src/components/QuestionScreen/`

## HighscoreScreen

**Purpose:** Speed-survival mode with shrinking per-question timer.

**Inputs:** None — always uses verified English single-select variants.

**Outputs:** Navigates to `/highscore-results` on wrong answer or timeout.

**Side effects:** Uses `requestAnimationFrame` for client-side countdown.

**Analytics events:** `highscore_start`, `highscore_end`.

**Location:** `src/components/HighscoreScreen/`

## HighscoreResults

**Purpose:** Shows Highscore run results and handles personal-best leaderboard submission.

**Inputs (via location.state):**
- `score: number`
- `questionsAnswered: number`
- `reason: 'timeout' | 'wrong' | null`

**Outputs:** Writes to `/leaderboard/{lang}/entries/{uid}` if new best.

**Location:** `src/components/HighscoreResults/`

## Leaderboard

**Purpose:** Public, language-scoped Highscore leaderboard.

**Inputs:** None.

**Outputs:** Ranks entries by score.

**Location:** `src/components/Leaderboard/`

## Settings

**Purpose:** User profile settings: preferred language and public leaderboard name.

**Inputs:** None — reads from auth and Firestore user profile.

**Outputs:** Updates `users/{uid}` and can sign the user out.

**Location:** `src/components/Settings/`

## PrivateRoute

**Purpose:** Route guard that redirects unauthenticated users to `/`.

**Location:** `src/components/PrivateRoute/`

## SignInScreen

**Purpose:** Entry point with Google Sign-In.

**Location:** `src/components/SignInScreen/`
