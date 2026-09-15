export default function RedFlags({ flags }) {
  if (!flags.length) return <div className="empty-flags">No strong red flags detected in this message.</div>
  return <div className="flags-list">{flags.map((flag) => (
    <article className="flag" key={`${flag.category}-${flag.evidence}`}>
      <div className="flag-icon">!</div>
      <div className="flag-copy"><strong>{flag.category}</strong><p>{flag.description}</p><blockquote>“{flag.evidence}”</blockquote></div>
      <span className="flag-score">+{flag.score}</span>
    </article>
  ))}</div>
}