import { useState } from 'react'
import Header from './components/Header'
import MessageInput from './components/MessageInput'
import RiskResult from './components/RiskResult'
import DemoMessages from './components/DemoMessages'
import SafeAction from './components/SafeAction'
import { analyzeMessage } from './services/api'

export default function App() {
  const [message, setMessage] = useState('')
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')

  async function handleAnalyze() {
    if (!message.trim()) return
    setLoading(true); setError('')
    try { setResult(await analyzeMessage(message)) } catch (analysisError) { setError(analysisError.message) } finally { setLoading(false) }
  }

  return <><Header /><main className="page-shell"><section className="hero"><div className="hero-kicker"><span /> MeitY / I4C TSTACK Hackathon PS06</div><h1>Pause before<br /><em>you click.</em></h1><p>Check suspicious SMS, emails and chat messages before they become a costly mistake.</p></section><div className="workspace"><div className="workspace-main"><MessageInput message={message} setMessage={(value) => { setMessage(value); setResult(null); setError('') }} onAnalyze={handleAnalyze} loading={loading} />{error && <div className="error-box" role="alert">{error}</div>}{result && <RiskResult result={result} />}</div><aside className="workspace-side"><SafeAction /><DemoMessages onSelect={(demo) => { setMessage(demo); setResult(null); setError('') }} /></aside></div></main><footer className="site-footer"><span>Digital Fraud Message Shield</span><span>Transparent rules. Safer choices.</span></footer></>
}