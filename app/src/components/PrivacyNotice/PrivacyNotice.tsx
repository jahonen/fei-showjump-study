import { useNavigate } from 'react-router-dom';
import './PrivacyNotice.scss';

/**
 * Minimum viable GDPR Privacy Notice for the ShowJump Study app.
 * Controller: CVPE Development Ltd (Finnish business ID 3651473-2).
 * Contact: dpo@cvpe.dev
 */
export default function PrivacyNotice() {
  const navigate = useNavigate();

  return (
    <main className="privacy-notice" role="main" aria-labelledby="privacy-title">
      <h1 id="privacy-title">Privacy Notice</h1>
      <p className="privacy-updated">Last updated: 13 September 2026</p>

      <section aria-labelledby="controller-heading">
        <h2 id="controller-heading">1. Who we are</h2>
        <p>
          This application is produced by <strong>CVPE Development Ltd</strong>, a company
          registered in Finland (business ID 3651473-2). We are the data controller for the
          personal data processed through this app.
        </p>
        <p>
          Data privacy contact:{' '}
          <a href="mailto:dpo@cvpe.dev">dpo@cvpe.dev</a>
        </p>
      </section>

      <section aria-labelledby="data-heading">
        <h2 id="data-heading">2. What personal data we collect</h2>
        <ul>
          <li>Google account display name and email address</li>
          <li>Your chosen public leaderboard name (optional)</li>
          <li>Study session results, review flags, and progress history</li>
          <li>Highscore scores and leaderboard entries</li>
        </ul>
      </section>

      <section aria-labelledby="purpose-heading">
        <h2 id="purpose-heading">3. Why we process your data and legal basis</h2>
        <table>
          <thead>
            <tr>
              <th scope="col">Purpose</th>
              <th scope="col">Legal basis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Provide user accounts and sign-in</td>
              <td>Performance of contract / legitimate interest</td>
            </tr>
            <tr>
              <td>Store study progress, attempts, and review flags</td>
              <td>Performance of contract</td>
            </tr>
            <tr>
              <td>Display public leaderboard entries</td>
              <td>Consent (public name and score are shown to other users)</td>
            </tr>
            <tr>
              <td>App analytics and error logging</td>
              <td>Legitimate interest</td>
            </tr>
          </tbody>
        </table>
      </section>

      <section aria-labelledby="recipients-heading">
        <h2 id="recipients-heading">4. Recipients and subprocessors</h2>
        <p>
          We use Firebase (Google Cloud) for authentication, database, and hosting. Firebase acts
          as a subprocessor. Core user and study data is stored in Firestore in the{' '}
          <code>eur3</code> European multi-region. Authentication and some Google Cloud
          infrastructure services may involve limited processing outside the EEA under the
          European Commission&apos;s adequacy decisions and/or Standard Contractual Clauses.
        </p>
      </section>

      <section aria-labelledby="retention-heading">
        <h2 id="retention-heading">5. Retention</h2>
        <p>
          We keep your account and study data for as long as your account is active. You can delete
          your account at any time by contacting us at{' '}
          <a href="mailto:dpo@cvpe.dev">dpo@cvpe.dev</a>. Public leaderboard entries are kept
          until you request deletion or replace them with a higher score.
        </p>
      </section>

      <section aria-labelledby="rights-heading">
        <h2 id="rights-heading">6. Your rights</h2>
        <p>Under the GDPR, you have the right to:</p>
        <ul>
          <li>Access the personal data we hold about you</li>
          <li>Correct inaccurate or incomplete data</li>
          <li>Request erasure of your data (&quot;right to be forgotten&quot;)</li>
          <li>Restrict or object to processing</li>
          <li>Receive your data in a portable format</li>
          <li>Withdraw consent at any time (this does not affect processing already carried out)</li>
          <li>Lodge a complaint with the Finnish Data Protection Ombudsman</li>
        </ul>
        <p>
          To exercise your rights, contact{' '}
          <a href="mailto:dpo@cvpe.dev">dpo@cvpe.dev</a>.
        </p>
      </section>

      <section aria-labelledby="cookies-heading">
        <h2 id="cookies-heading">7. Cookies and local storage</h2>
        <p>
          The app uses Firebase Authentication tokens and a small amount of local/browser storage
          to keep you signed in and to support offline caching of the current study session. No
          third-party advertising cookies are used.
        </p>
      </section>

      <section aria-labelledby="changes-heading">
        <h2 id="changes-heading">8. Changes to this notice</h2>
        <p>
          We may update this notice from time to time. The latest version is always available in
          the app and from the same URL.
        </p>
      </section>

      <button type="button" className="back-button" onClick={() => navigate(-1)}>
        Back
      </button>
    </main>
  );
}
