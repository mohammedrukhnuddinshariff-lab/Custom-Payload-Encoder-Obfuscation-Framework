import re
from typing import Iterable


def detect_signature(text: str, signatures: Iterable[str]) -> list[str]:
    """
    Perform a basic case-insensitive signature check.
    """
    detected = []

    for signature in signatures:
        if signature.lower() in text.lower():
            detected.append(signature)

    return detected


def normalize_text(text: str) -> str:
    """
    Normalize text for defensive comparison.

    Removes non-alphanumeric characters and converts
    the text to lowercase.
    """
    return re.sub(r"[^a-zA-Z0-9]", "", text).lower()


def detect_normalized(text: str, signatures: Iterable[str]) -> list[str]:
    """
    Detect signatures after basic normalization.
    """
    normalized_text = normalize_text(text)

    detected = []

    for signature in signatures:
        normalized_signature = normalize_text(signature)

        if normalized_signature in normalized_text:
            detected.append(signature)

    return detected


def is_detected(text: str, signatures: Iterable[str]) -> bool:
    """
    Return True if a direct signature matches.
    """
    return bool(detect_signature(text, signatures))