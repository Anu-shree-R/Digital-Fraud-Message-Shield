"""Pydantic request and response schemas for the API."""

from pydantic import BaseModel, Field, field_validator


class AnalyzeRequest(BaseModel):
    message: str = Field(..., max_length=5000)

    @field_validator("message")
    @classmethod
    def message_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Message cannot be empty or whitespace-only.")
        return value


class DetectedFlag(BaseModel):
    category: str
    description: str
    evidence: str
    score: int


class AnalyzeResponse(BaseModel):
    risk_score: int
    risk_level: str
    scam_type: str
    detected_flags: list[DetectedFlag]
    recommended_action: str
    summary: str