def insert_separator(text: str, separator: str = "|") -> str:
    """
    Insert a separator between characters.
    """
    if not separator:
        raise ValueError("Separator cannot be empty.")

    return separator.join(text)


def remove_separator(text: str, separator: str = "|") -> str:
    """
    Remove the inserted separator and recover the original string.
    """
    return text.replace(separator, "")