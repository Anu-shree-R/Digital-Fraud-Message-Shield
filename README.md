# Digital Fraud Message Shield

Rule-based digital fraud message detection for TSTACK Hackathon PS06, Ministry of Electronics & IT (MeitY) / I4C.

## Problem

Citizens often receive fraudulent SMS, email, and chat messages and need a quick way to determine whether a message is suspicious.

## Solution

Paste an SMS, email, or chat message and receive a deterministic risk score, risk level, scam classification, matched evidence, explainable red flags, and a safe next action. The detector uses transparent regex, keywords, pattern matching, and URL inspection. It does not use AI, machine learning, paid APIs, or network access to analyzed links.

## Features

- Risk score
- Risk level
- Scam type classification
- Red-flag detection
- Evidence highlighting
- Safe next-step recommendations
- Rule-based explainable detection
- Synthetic test dataset

The frontend is deliberately thin: it submits the pasted message and renders the backend response. Evidence is inserted as React text nodes, so user content is escaped safely by the browser.

## Detection engine and scoring

`backend/app/rules.py` contains extendable rule records with an ID, category, regex, score, and explanation. Each rule matches once to avoid repeated-keyword double counting. URL analysis is local only and checks HTTP, shorteners, IP hosts, punycode, many subdomains, and selected high-risk TLDs.

Score levels are LOW (0-29), MEDIUM (30-59), HIGH (60-79), and CRITICAL (80-100). The final score is capped at 100. Safe examples such as an OTP reminder, completed UPI payment, and bank payment notification are supported without treating banking words alone as a scam request.

Classifications include Banking / KYC Phishing, UPI / Payment Scam, Job Scam, Courier / Delivery Scam, Lottery / Prize Scam, Government / Police Impersonation, Account / Credential Phishing, Investment Scam, Tech Support Scam, Generic Phishing, and Safe / No Strong Scam Indicators.

## Technology Stack

- React + Vite
- Python + FastAPI
- Rule-based keyword and regex detection
- Pytest

## Project Structure

```text
backend/   - FastAPI app, rule engine, and pytest tests
frontend/  - React/Vite web interface
data/      - Synthetic labelled test messages
```

## API

`GET /api/health` returns `{ "status": "ok" }`.

`POST /api/analyze` accepts `{ "message": "..." }`, rejects blank messages and messages over 5,000 characters, and returns the score, level, scam type, flags, action, and summary.

## Installation and local run

Backend in PowerShell:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend in a second terminal:

```powershell
cd frontend
npm install
npm run dev
```

The default frontend API URL is `http://localhost:8000`. Open the Vite URL, choose a synthetic demo or paste a message, and select **Check message**.

## Dataset and testing

`data/test_messages.csv` contains 25 synthetic scam, safe, and borderline examples covering Indian fraud terminology and safe false-positive cases. It contains no real personal, account, credential, or financial records.

```powershell
cd backend
python -m pytest -q
```

## Deployment, limitations, and disclaimer

Deploy FastAPI with an ASGI server behind HTTPS and serve `frontend/dist` after `npm run build`. Set `VITE_API_URL` to the deployed API and update the CORS allowlist.

Rules cannot understand every language, context, sender identity, or newly invented scam. An unusual domain is not automatically malicious, and a low score is not a guarantee of safety. Future work could add multilingual rule packs, reviewed rule management, and trusted domain reputation data while preserving explainability and privacy.

This is educational decision support, not a substitute for a bank, platform, police, or cybersecurity investigation. Verify unexpected requests through official channels.

```

Suggested root `.gitignore`:

```text
__pycache__/
*.py[cod]

.venv/
venv/
env/

.env
.env.*

node_modules/
dist/
build/

.vscode/
.idea/

*.log
.pytest_cache/
.coverage
htmlcov/

.DS_Store
Thumbs.db