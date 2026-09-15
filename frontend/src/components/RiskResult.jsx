import RiskScore from './RiskScore'
import RedFlags from './RedFlags'

export default function RiskResult({ result }) {
  return <section className="results" aria-live="polite">
    <div className="result-heading"><div><p className="eyebrow">Analysis complete</p><h2>Your message, decoded.</h2></div><span className="result-pill">{result.scam_type}</span></div>
    <div className="result-grid"><RiskScore score={result.risk_score} level={result.risk_level} /><div className="summary-panel"><p className="eyebrow">What we found</p><p className="summary">{result.summary}</p><div className="action-box"><span className="action-icon">&#10003;</span><div><p className="eyebrow">Recommended action</p><p>{result.recommended_action}</p></div></div></div></div>
    <div className="flags-section"><div className="section-title"><h3>Red flags detected</h3><span>{result.detected_flags.length} signals</span></div><RedFlags flags={result.detected_flags} /></div>
    <details className="breakdown"><summary><span>Why was this message flagged?</span><span className="summary-arrow">+</span></summary><div className="breakdown-content">{result.detected_flags.length ? result.detected_flags.map((flag) => <div className="breakdown-row" key={flag.category}><span>{flag.category}</span><b>+{flag.score}</b></div>) : <p>No score contribution.</p>}<div className="breakdown-total"><span>Final risk score</span><b>{result.risk_score} / 100</b></div></div></details>
  </section>
}