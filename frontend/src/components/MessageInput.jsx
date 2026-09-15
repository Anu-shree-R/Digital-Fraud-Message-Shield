export default function MessageInput({ message, setMessage, onAnalyze, loading }) {
  return (
    <form className="inspection-console" onSubmit={(event) => { event.preventDefault(); onAnalyze() }}>
      <div className="console-heading">
        <div className="console-title"><span className="label-number">01</span><div><p className="eyebrow">Message inspection</p><h2>Paste a suspicious message</h2></div></div>
        <span className="console-mode">Local analysis</span>
      </div>
      <p className="console-helper">SMS, email, WhatsApp or chat — up to 5,000 characters.</p>
      <textarea
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        maxLength={5000}
        placeholder="Paste the message content here..."
        aria-label="Message to analyze"
      />
      <div className="input-footer">
        <span className="counter"><span className="input-lock" aria-hidden="true">*</span>{message.length.toLocaleString()} / 5,000</span>
        <div className="input-actions">
          <button type="button" className="button button-quiet" onClick={() => setMessage('')} disabled={!message}>Clear</button>
          <button type="submit" className="button button-primary" disabled={loading || !message.trim()}>
            {loading ? <><span className="button-spinner" aria-hidden="true" /> Analyzing...</> : <>Analyze message <span aria-hidden="true">-&gt;</span></>}
          </button>
        </div>
      </div>
      <p className="console-hint"><span aria-hidden="true">*</span> Links are analyzed locally. We never open or fetch them.</p>
    </form>
  )
}