import "./About.css";

export default function About() {
  return (
    <div className="about-container">
      <div className="about-card">
        <h1>About This App</h1>
        <p>
          This is a full-stack AI Chat application built as a student project. It allows
          users to have a continuous AI-powered conversation, powered by OpenAI's API.
        </p>

        <h2>Tech Stack</h2>
        <ul>
          <li><strong>Frontend:</strong> React + TypeScript (SPA) + React Router</li>
          <li><strong>Backend:</strong> Python FastAPI (REST API)</li>
          <li><strong>Database:</strong> MySQL — stores all conversations and messages</li>
          <li><strong>AI:</strong> OpenAI GPT-4o-mini via OpenAI Python SDK</li>
        </ul>

        <h2>Developer</h2>
        <p>
          Built by a Full Stack Web Development student as Project #4.
        </p>
      </div>
    </div>
  );
}
