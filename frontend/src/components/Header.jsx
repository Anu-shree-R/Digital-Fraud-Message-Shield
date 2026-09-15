export default function Header() {
  return (
    <header className="site-header">
      <a className="brand" href="/" aria-label="Digital Fraud Message Shield home">
        <span className="brand-mark" aria-hidden="true"><span /></span>
        <span className="brand-copy"><b>Digital Fraud</b><strong>Message Shield</strong></span>
      </a>
      <div className="header-status"><span className="status-dot" /> <span>Rule-based engine</span><b>Online</b></div>
    </header>
  )
}