import "./Message.css";

interface MessageProps {
  role: "user" | "assistant";
  content: string;
}

export default function Message({ role, content }: MessageProps) {
  const isUser = role === "user";
  return (
    <div className={`message-row ${isUser ? "user-row" : "assistant-row"}`}>
      <div className={`message-bubble ${isUser ? "user-bubble" : "assistant-bubble"}`}>
        <span className="message-label">{isUser ? "You" : "AI"}</span>
        <p className="message-text">{content}</p>
      </div>
    </div>
  );
}
