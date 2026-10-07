def xor_transform(text: str, key: int) -> str:
    """
    Apply a reversible XOR transformation to a text string.

    The same function is used for both transformation
    and recovery of the original text.
    """
    if not 0 <= key <= 255:
        raise ValueError("Key must be between 0 and 255.")

    result = []

    for character in text:
        transformed = ord(character) ^ key
        result.append(chr(transformed))

    return "".join(result)