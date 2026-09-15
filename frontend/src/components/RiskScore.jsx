export default function RiskScore({ score, level }) {
  return (
    <div className={`score-panel level-${level.toLowerCase()}`}>
      <div className="score-orbit" aria-hidden="true"><span>{score}</span></div>
      <div><p className="eyebrow">Risk score</p><p className="score-value">{score}<small>/100</small></p><p className="score-level">{level} risk</p></div>
    </div>
  )
}