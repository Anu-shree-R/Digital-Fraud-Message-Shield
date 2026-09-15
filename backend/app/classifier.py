"""Deterministic scam classification and safe action recommendations."""


def classify(signal_ids: set[str]) -> str:
    if {"job", "payment"} <= signal_ids:
        return "Job Scam"
    if {"courier", "payment"} <= signal_ids:
        return "Courier / Delivery Scam"
    if {"reward", "payment"} <= signal_ids:
        return "Lottery / Prize Scam"
    if "government" in signal_ids and ("threat" in signal_ids or "payment" in signal_ids):
        return "Government / Police Impersonation"
    if "investment" in signal_ids and ("payment" in signal_ids or "upi" in signal_ids):
        return "Investment Scam"
    if "tech_support" in signal_ids:
        return "Tech Support Scam"
    if "kyc" in signal_ids and ("banking" in signal_ids or "threat" in signal_ids or "url" in signal_ids or "urgency" in signal_ids):
        return "Banking / KYC Phishing"
    if "upi" in signal_ids and ("payment" in signal_ids or "credential_request" in signal_ids):
        return "UPI / Payment Scam"
    if "credential_request" in signal_ids or "otp_request" in signal_ids:
        return "Account / Credential Phishing"
    if "url" in signal_ids:
        return "Generic Phishing"
    return "Safe / No Strong Scam Indicators"


def recommended_action(scam_type: str) -> str:
    actions = {
        "Banking / KYC Phishing": "Do not click the link or share OTP, PIN, CVV or password. Verify through your bank's official app or website.",
        "UPI / Payment Scam": "Do not approve unexpected payment or collect requests. Verify the recipient in your official payment app.",
        "Job Scam": "Do not pay registration or processing fees for an unexpected job offer. Verify the employer through its official website.",
        "Courier / Delivery Scam": "Do not pay unexpected customs or delivery charges through a message link. Verify the shipment through the courier's official website.",
        "Lottery / Prize Scam": "Do not pay a fee to claim an unexpected prize. Do not share banking credentials.",
        "Government / Police Impersonation": "Do not transfer money or share personal details because of a threat. Contact the department through its official website.",
        "Investment Scam": "Do not send money based on guaranteed returns or unsolicited tips. Verify any investment with a regulated provider.",
        "Tech Support Scam": "Do not install software or grant remote access from an unsolicited message. Contact support through an official channel.",
        "Account / Credential Phishing": "Do not click suspicious links or share OTP, passwords, or card details. Verify through the official app or website.",
        "Generic Phishing": "Do not click suspicious links or provide personal information. Verify the message through an official channel.",
    }
    return actions.get(scam_type, "No strong scam indicators were detected. Still verify unexpected requests through official channels.")