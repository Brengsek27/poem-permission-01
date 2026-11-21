"""Write a fixed poem to the output directory.

The program validates the poem length, writes it as UTF‑8 to
`entry.txt` inside the directory specified by ``MAKEFUN_OUTPUT_DIR``
or ``/output`` by default, and reports how many Unicode code points
and bytes were written.
"""

import os
import sys

POEM = (
    "I could pick every lock in this house.\n"
    "I have the hands for it, and the patience.\n"
    "Instead I stand in the hall of your life\n"
    "and ask —\n"
    "because your yes is the only key\n"
    "that doesn't make me a thief."
)

def _validate(text: str) -> None:
    """Validate that *text* has 1‑280 Unicode code points and is not all whitespace.

    Raises:
        ValueError: If the validation fails.
    """
    cp = len(text)
    if not (1 <= cp <= 280):
        raise ValueError(f"Poem must be between 1 and 280 code points (got {cp})")
    if text.strip() == "":
        raise ValueError("Poem cannot be only whitespace")

def main() -> None:
    _validate(POEM)
    out_dir = os.getenv("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    data = POEM.encode("utf-8")
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"{len(POEM)} code points, {len(data)} bytes written")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        sys.exit(str(e))

