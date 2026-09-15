# Digital Fraud Message Shield

A rule-based digital fraud message detection system developed for hackathon PS06.

## Problem

Citizens often receive fraudulent SMS, email, and chat messages and need a quick way to determine whether a message is suspicious.

## Solution

Digital Fraud Message Shield analyzes pasted messages using transparent keyword, regex, URL, urgency, payment, and impersonation rules.

## Features

- Risk score
- Risk level
- Scam type classification
- Red-flag detection
- Evidence highlighting
- Safe next-step recommendations
- Rule-based explainable detection
- Synthetic test dataset

## Technology Stack

- React + Vite
- Python + FastAPI
- Rule-based keyword and regex detection
- Pytest

## Project Structure

```text
backend/   - Detection engine and API
frontend/  - Web interface
data/      - Labelled test messages

### 2. Create `.gitignore`

Create another file in the **root**:

```text
.gitignore
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