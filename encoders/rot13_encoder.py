def transform(text: str) -> str:
    """
    Apply ROT13 transformation.

    ROT13 is reversible, so applying the same
    transformation twice returns the original text.
    """
    result = []

    for character in text:
        if "A" <= character <= "Z":
            result.append(
                chr((ord(character) - ord("A") + 13) % 26 + ord("A"))
            )
        elif "a" <= character <= "z":
            result.append(
                chr((ord(character) - ord("a") + 13) % 26 + ord("a"))
            )
        else:
            result.append(character)

    return "".join(result)