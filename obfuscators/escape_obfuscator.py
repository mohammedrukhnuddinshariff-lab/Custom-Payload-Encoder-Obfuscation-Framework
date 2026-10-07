def to_hex_escape(text: str) -> str:
    """
    Convert text characters to hexadecimal escape representation.
    """
    return "".join(
        f"\\x{ord(character):02x}"
        for character in text
    )


def from_hex_escape(text: str) -> str:
    """
    Convert hexadecimal escape representation back to text.
    """
    if len(text) % 4 != 0:
        raise ValueError("Invalid hexadecimal escape representation.")

    result = []

    for i in range(0, len(text), 4):
        chunk = text[i:i + 4]

        if not chunk.startswith("\\x"):
            raise ValueError("Invalid escape sequence.")

        result.append(chr(int(chunk[2:], 16)))

    return "".join(result)