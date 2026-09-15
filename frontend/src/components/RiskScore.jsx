export default function RiskScore({ score, level }) {
  return (
    <div className={`score-panel level-${level.toLowerCase()}`}>
      <div className="score-panel-top"><p className="eyebrow">Risk score</p><span className="severity-badge">{level} risk</span></div>
      <div className="score-readout"><strong>{score}</strong><span>/ 100</span></div>
      <div className="score-instrument"><div className="score-track" aria-label={`${score} out of 100 risk score`}><span style={{ width: `${score}%` }} /><i className="score-tick tick-25" /><i className="score-tick tick-50" /><i className="score-tick tick-75" /></div><div className="score-scale"><span>0</span><span>50</span><span>100</span></div></div>
      <p className="score-caption">Deterministic signal confidence</p>
    </div>
  )
}