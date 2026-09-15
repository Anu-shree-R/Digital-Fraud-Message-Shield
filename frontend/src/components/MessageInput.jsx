export default function MessageInput({ message, setMessage, onAnalyze, loading }) {
  return (
    <form className="message-card" onSubmit={(event) => { event.preventDefault(); onAnalyze() }}>
      <div className="card-label"><span className="label-number">01</span><span>Paste a message to inspect</span></div>
      <textarea
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        maxLength={5000}
        placeholder="Paste an SMS, email, or chat message here..."
        aria-label="Message to analyze"
      />
      <div className="input-footer">
        <span className="counter">{message.length.toLocaleString()} / 5,000</span>
        <div className="input-actions">
          <button type="button" className="button button-quiet" onClick={() => setMessage('')} disabled={!message}>Clear</button>
          <button type="submit" className="button button-primary" disabled={loading || !message.trim()}>
            {loading ? 'Checking...' : 'Check message'} <span aria-hidden="true">-&gt;</span>
          </button>
        </div>
      </div>
    </form>
  )
}