const demos = [
  { label: 'Bank / KYC', tone: 'red', message: 'URGENT: Your bank account will be suspended today. Update KYC immediately at http://secure.example.xyz' },
  { label: 'Fake job', tone: 'orange', message: 'Work from home job offer! Pay a registration fee today to unlock your high salary.' },
  { label: 'Courier scam', tone: 'yellow', message: 'Your courier parcel is held in customs. Pay the delivery charge immediately through this link.' },
  { label: 'Prize scam', tone: 'pink', message: 'Congratulations, you are a lottery winner! Pay a small claim fee to receive your prize.' },
  { label: 'Everyday message', tone: 'green', message: 'Your OTP for login is 123456. Do not share this OTP with anyone.' },
]

export default function DemoMessages({ onSelect }) {
  return <section className="demo-section"><div className="section-title"><div><p className="eyebrow">Try a synthetic example</p><h3>Demo messages</h3></div><span>5 examples</span></div><div className="demo-grid">{demos.map((demo) => <button className="demo-card" key={demo.label} onClick={() => onSelect(demo.message)}><span className={`demo-dot ${demo.tone}`} /><span>{demo.label}</span><span className="demo-arrow">-&gt;</span></button>)}</div></section>
}