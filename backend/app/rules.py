"""Transparent detection rules used by the fraud message analyzer."""

from dataclasses import dataclass
import re


@dataclass(frozen=True)
class DetectionRule:
    rule_id: str
    category: str
    pattern: str
    score: int
    explanation: str
    flags: int = re.IGNORECASE


RULES = (
    DetectionRule("urgency", "Urgency", r"\b(?:urgent|immediately|right now|within \d+ (?:minutes?|hours?)|act now|last warning|expires? today)\b", 15, "The message creates time pressure to discourage careful verification."),
    DetectionRule("threat", "Threat / Fear", r"\b(?:blocked|suspended|deactivated|legal action|arrest|police case|penalty|fine|warrant|disconnected)\b", 20, "The message uses fear or a threat of loss to prompt action."),
    DetectionRule("payment", "Payment Request", r"\b(?:pay|payment|send|transfer|deposit|processing fee|registration fee|customs fee|delivery charge|claim fee)\b|₹\s?[\d,]+", 15, "The message asks for money or a fee in an unexpected context."),
    DetectionRule("otp_request", "OTP Request", r"(?!.*\b(?:do not|don't)\s+(?:share|send|tell|provide)\b)(?:\b(?:share|send|tell|provide|enter|verify)\b.{0,35}\bOTP\b|\bOTP\b.{0,35}\b(?:share|send|tell|provide|enter)\b)", 25, "A message asks the recipient to disclose or enter a one-time password."),
    DetectionRule("credential_request", "PIN / Password / CVV Request", r"\b(?:share|send|provide|confirm|enter|update)\b.{0,40}\b(?:PIN|password|passcode|CVV|card number|account number)\b", 25, "The message requests credentials or sensitive banking information."),
    DetectionRule("kyc", "KYC / Account Verification", r"\b(?:KYC|Aadhaar|PAN)\b.{0,50}\b(?:update|verify|complete|expire|link|submit)\b|\b(?:update|verify|complete|expire)\b.{0,50}\b(?:KYC|Aadhaar|PAN)\b", 20, "The message uses identity verification as a reason to request action."),
    DetectionRule("url", "Suspicious URL", r"https?://[^\s<>\"']+|\b(?:www\.)[a-z0-9.-]+\.[a-z]{2,}(?:/[^\s<>\"']*)?", 20, "The message contains a link that needs careful verification before opening."),
    DetectionRule("impersonation", "Impersonation", r"\b(?:dear customer|official notice|security team|support team|account department|verification team)\b", 10, "The sender presents a generic authority or support identity."),
    DetectionRule("reward", "Reward / Lottery / Prize", r"\b(?:winner|won|lottery|prize|reward|cashback|lucky draw|claim your)\b", 20, "The message promises an unexpected reward or prize."),
    DetectionRule("job", "Job Offer", r"\b(?:job offer|work from home|part[- ]time job|hiring|vacancy|salary|registration fee|joining fee)\b", 15, "The message presents an unsolicited job or income opportunity."),
    DetectionRule("courier", "Courier / Delivery", r"\b(?:courier|delivery|parcel|package|shipment|customs|consignment|fastag)\b", 15, "The message references a delivery or shipment that may be used to request payment."),
    DetectionRule("government", "Government / Police Impersonation", r"\b(?:police|income tax|government|RBI|cyber crime|court|customs officer)\b", 20, "The message invokes a government, police, or regulatory authority."),
    DetectionRule("upi", "UPI / Payment", r"\b(?:UPI|QR code|scan the QR|collect request|UPI ID|Google Pay|PhonePe|Paytm)\b", 15, "The message references a digital payment mechanism."),
    DetectionRule("banking", "Banking", r"\b(?:bank account|banking|net banking|debit card|credit card|account blocked|account suspended|IFSC)\b", 15, "The message references a bank account or banking service."),
    DetectionRule("investment", "Investment", r"\b(?:investment|invest|trading|stock tips?|crypto|guaranteed returns?|double your money|profit)\b", 20, "The message promotes an investment or unusually certain financial return."),
    DetectionRule("tech_support", "Tech Support", r"\b(?:technical support|tech support|virus|malware|remote access|computer infected|customer care)\b", 15, "The message claims a technical problem or support emergency."),
)