import pytest
from fastapi.testclient import TestClient
from app.detector import analyze_message
from app.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    ("message", "scam_type"),
    [
        ("URGENT: Your bank account is suspended. Update KYC immediately at http://secure.example.xyz", "Banking / KYC Phishing"),
        ("Complete KYC verification now or your Aadhaar account will be blocked.", "Banking / KYC Phishing"),
        ("Scan this UPI QR code and send payment immediately to receive your refund.", "UPI / Payment Scam"),
        ("Work from home job offer. Pay a registration fee today to start your salary.", "Job Scam"),
        ("Your courier is held in customs. Pay the delivery charge immediately.", "Courier / Delivery Scam"),
        ("Congratulations, you are a lottery winner. Pay a claim fee to receive the prize.", "Lottery / Prize Scam"),
        ("Police case is pending. Transfer the penalty immediately to avoid arrest.", "Government / Police Impersonation"),
        ("Share your password and OTP to keep your account active.", "Account / Credential Phishing"),
        ("Invest now for guaranteed returns and double your money. Send payment today.", "Investment Scam"),
        ("Your computer has a virus. Call technical support and install remote access.", "Tech Support Scam"),
    ],
)
def test_scam_classification(message, scam_type):
    result = analyze_message(message)
    assert result["scam_type"] == scam_type
    assert 0 <= result["risk_score"] <= 100
    assert result["detected_flags"]
    assert all(flag["evidence"] in message for flag in result["detected_flags"])


@pytest.mark.parametrize("message", ["Your OTP for login is 123456. Do not share this OTP with anyone.", "I paid ₹500 using UPI to the grocery store.", "Your bank payment of ₹500 was completed successfully.", "Can we meet for tea tomorrow afternoon?"])
def test_safe_messages_are_not_high_risk(message):
    result = analyze_message(message)
    assert result["risk_score"] < 60
    if "Do not share this OTP" in message:
        assert result["scam_type"] == "Safe / No Strong Scam Indicators"


def test_suspicious_url_has_evidence_and_url_flag():
    result = analyze_message("Verify your account urgently at http://192.168.1.1/login")
    assert any(flag["category"] == "Suspicious URL" for flag in result["detected_flags"])
    assert any("192.168.1.1" in flag["evidence"] for flag in result["detected_flags"])


def test_repeated_keywords_are_not_double_counted():
    assert analyze_message("URGENT urgent URGENT act now")["risk_score"] == 15


def test_api_validation_and_health():
    assert client.get("/api/health").json() == {"status": "ok"}
    assert client.post("/api/analyze", json={"message": "   "}).status_code == 422
    assert client.post("/api/analyze", json={"message": "x" * 5001}).status_code == 422


def test_mixed_case_message_is_detected():
    assert analyze_message("uRgEnT: sHaRe your OTP immediately")["risk_level"] in {"MEDIUM", "HIGH", "CRITICAL"}