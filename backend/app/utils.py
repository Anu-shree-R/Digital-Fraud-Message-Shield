"""Small pure helpers for safe, deterministic message inspection."""

import re
from urllib.parse import urlparse

URL_PATTERN = re.compile(r"https?://[^\s<>\"']+|\b(?:www\.)[a-z0-9.-]+\.[a-z]{2,}(?:/[^\s<>\"']*)?", re.IGNORECASE)


def first_match(pattern: str, message: str, flags: int = re.IGNORECASE) -> str | None:
    match = re.search(pattern, message, flags)
    return match.group(0).rstrip(".,);!") if match else None


def extract_urls(message: str) -> list[str]:
    return [match.rstrip(".,);!") for match in URL_PATTERN.findall(message)]


def url_reasons(url: str) -> list[str]:
    candidate = url if "://" in url else f"http://{url}"
    parsed = urlparse(candidate)
    host = (parsed.hostname or "").lower().rstrip(".")
    reasons: list[str] = []
    if parsed.scheme == "http":
        reasons.append("uses HTTP instead of HTTPS")
    if host in {"localhost", "example.com", "example.org", "example.net"}:
        return reasons
    if host in {"bit.ly", "tinyurl.com", "t.co", "shorturl.at", "is.gd", "ow.ly"}:
        reasons.append("uses a URL-shortening service")
    if re.fullmatch(r"\d{1,3}(?:\.\d{1,3}){3}", host):
        reasons.append("uses an IP address instead of a domain")
    if any(host.endswith(tld) for tld in (".xyz", ".top", ".click", ".buzz", ".tk", ".gq", ".work", ".zip")):
        reasons.append("uses a less common high-risk TLD")
    if "xn--" in host:
        reasons.append("contains punycode")
    if len(host.split(".")) > 4:
        reasons.append("contains many subdomains")
    return reasons


def risk_level(score: int) -> str:
    if score >= 80:
        return "CRITICAL"
    if score >= 60:
        return "HIGH"
    if score >= 30:
        return "MEDIUM"
    return "LOW"