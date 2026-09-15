"""Explainable rule-based fraud message detector."""

import re
from .classifier import classify, recommended_action
from .rules import RULES
from .utils import extract_urls, first_match, risk_level, url_reasons


class MessageDetector:
    def analyze(self, message: str) -> dict:
        flags: list[dict] = []
        signal_ids: set[str] = set()
        for rule in RULES:
            evidence = first_match(rule.pattern, message, rule.flags)
            if rule.rule_id == "otp_request" and re.search(r"\b(?:do not|don't)\s+(?:share|send|tell|provide)\b", message, re.IGNORECASE):
                evidence = None
            if evidence:
                description = rule.explanation
                score = rule.score
                if rule.rule_id == "url":
                    urls = extract_urls(message)
                    reasons = url_reasons(urls[0]) if urls else []
                    description = f"{description} " + ("Signals: " + ", ".join(reasons) + "." if reasons else "It is not automatically malicious, but verify the destination before opening.")
                    score = min(rule.score + (5 if reasons else 0), 25)
                flags.append({"category": rule.category, "description": description, "evidence": evidence, "score": score})
                signal_ids.add(rule.rule_id)

        score = min(sum(flag["score"] for flag in flags), 100)
        scam_type = classify(signal_ids)
        level = risk_level(score)
        summary = "No strong scam indicators were found in this message." if not flags else f"Found {len(flags)} explainable signal{'s' if len(flags) != 1 else ''}; review the message before taking action."
        return {"risk_score": score, "risk_level": level, "scam_type": scam_type, "detected_flags": flags, "recommended_action": recommended_action(scam_type), "summary": summary}


def analyze_message(message: str) -> dict:
    return MessageDetector().analyze(message)