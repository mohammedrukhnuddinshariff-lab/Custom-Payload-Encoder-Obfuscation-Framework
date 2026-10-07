def split_string(text: str, chunk_size: int = 3) -> list[str]:
    """
    Split a string into fixed-size chunks.
    """
    if chunk_size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    return [
        text[i:i + chunk_size]
        for i in range(0, len(text), chunk_size)
    ]


def join_chunks(chunks: list[str]) -> str:
    """
    Reconstruct the original string from chunks.
    """
    return "".join(chunks)