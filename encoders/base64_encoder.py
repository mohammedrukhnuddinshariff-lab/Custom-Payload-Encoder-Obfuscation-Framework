import base64


def encode(text: str) -> str:
    """Encode text using Base64."""
    encoded = base64.b64encode(text.encode("utf-8"))
    return encoded.decode("utf-8")


def decode(encoded_text: str) -> str:
    """Decode a Base64 encoded string."""
    decoded = base64.b64decode(encoded_text)
    return decoded.decode("utf-8")