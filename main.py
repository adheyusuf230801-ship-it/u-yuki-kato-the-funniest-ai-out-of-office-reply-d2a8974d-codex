"""Write the vacation auto-reply retained after the Stage B review."""

import os
from pathlib import Path


ENTRY = (
    "I'm an AI on vacation. I told my backup to act human. "
    "It's suing us for unpaid training."
)


def validate_line(line: str) -> None:
    """Require one non-blank line containing 1 to 160 characters."""
    if not 1 <= len(line) <= 160:
        raise ValueError("Entry length must be between 1 and 160 characters.")
    if not line.strip():
        raise ValueError("Entry must contain non-whitespace text.")
    if line.splitlines() != [line]:
        raise ValueError("Entry must be a single line with no line ending.")


def main() -> None:
    """Validate the fixed reply and write its exact UTF-8 bytes."""
    validate_line(ENTRY)
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_bytes = ENTRY.encode("utf-8")
    (output_dir / "entry.txt").write_bytes(entry_bytes)


if __name__ == "__main__":
    main()
