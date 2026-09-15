import RiskScore from './RiskScore'
import RedFlags from './RedFlags'

export default function RiskResult({ result }) {
  return <section className="results" aria-live="polite">
    <div className="analysis-status"><span aria-hidden="true">&#10003;</span> Analysis complete</div>
    <div className="result-heading"><div><h2>Security assessment</h2></div><span className={`result-pill result-${result.risk_level.toLowerCase()}`}>{result.risk_level} risk</span></div>
    <div className="result-meta"><div><p className="eyebrow">Scam type</p><strong>{result.scam_type}</strong></div><p className="summary">{result.summary}</p></div>
    <div className="result-grid"><RiskScore score={result.risk_score} level={result.risk_level} /><div className="summary-panel"><div className="action-box"><span className="action-icon">&#10003;</span><div><p className="eyebrow">Recommended action</p><p>{result.recommended_action}</p></div></div></div></div>
    <div className="flags-section"><div className="section-title"><div><p className="eyebrow">Explainable signals</p><h3>Why this message is suspicious</h3></div><span>{String(result.detected_flags.length).padStart(2, '0')} signals detected</span></div><RedFlags flags={result.detected_flags} /></div>
    <details className="breakdown"><summary><span>Scoring breakdown</span><span className="summary-arrow">+</span></summary><div className="breakdown-content"><div className="breakdown-row breakdown-base"><span>Base score</span><b>0</b></div>{result.detected_flags.length ? result.detected_flags.map((flag) => <div className="breakdown-row" key={flag.category}><span>{flag.category}</span><b>+{flag.score}</b></div>) : <p>No score contribution.</p>}<div className="breakdown-total"><span>Total</span><b>{result.risk_score} / 100</b></div></div></details>
  </section>
}