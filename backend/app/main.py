"""FastAPI entry point for Digital Fraud Message Shield."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .detector import analyze_message
from .schemas import AnalyzeRequest, AnalyzeResponse


app = FastAPI(
    title="Digital Fraud Message Shield API",
    version="1.0.0",
)


# Allow requests from the local frontend and the deployed Vercel frontend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://digital-fraud-message-shield.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    return AnalyzeResponse(**analyze_message(request.message))