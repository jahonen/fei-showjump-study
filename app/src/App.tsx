import { Routes, Route } from 'react-router-dom';
import SignInScreen from '@/components/SignInScreen/SignInScreen';
import Dashboard from '@/components/Dashboard/Dashboard';
import FreeStudySetup from '@/components/FreeStudySetup/FreeStudySetup';
import QuestionScreen from '@/components/QuestionScreen/QuestionScreen';
import TimedTrialResults from '@/components/TimedTrialResults/TimedTrialResults';
import ReviewQueue from '@/components/ReviewQueue/ReviewQueue';
import HighscoreScreen from '@/components/HighscoreScreen/HighscoreScreen';
import HighscoreResults from '@/components/HighscoreResults/HighscoreResults';
import Leaderboard from '@/components/Leaderboard/Leaderboard';
import Settings from '@/components/Settings/Settings';
import PrivacyNotice from '@/components/PrivacyNotice/PrivacyNotice';
import PrivateRoute from '@/components/PrivateRoute/PrivateRoute';

function App() {
  return (
    <div className="app">
      <Routes>
        <Route path="/" element={<SignInScreen />} />
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/free-study"
          element={
            <PrivateRoute>
              <FreeStudySetup />
            </PrivateRoute>
          }
        />
        <Route
          path="/study"
          element={
            <PrivateRoute>
              <QuestionScreen />
            </PrivateRoute>
          }
        />
        <Route
          path="/timed-results"
          element={
            <PrivateRoute>
              <TimedTrialResults />
            </PrivateRoute>
          }
        />
        <Route
          path="/review"
          element={
            <PrivateRoute>
              <ReviewQueue />
            </PrivateRoute>
          }
        />
        <Route
          path="/highscore"
          element={
            <PrivateRoute>
              <HighscoreScreen />
            </PrivateRoute>
          }
        />
        <Route
          path="/highscore-results"
          element={
            <PrivateRoute>
              <HighscoreResults />
            </PrivateRoute>
          }
        />
        <Route
          path="/leaderboard"
          element={
            <PrivateRoute>
              <Leaderboard />
            </PrivateRoute>
          }
        />
        <Route
          path="/settings"
          element={
            <PrivateRoute>
              <Settings />
            </PrivateRoute>
          }
        />
        <Route path="/privacy" element={<PrivacyNotice />} />
      </Routes>
    </div>
  );
}

export default App;
