"""news-image-20261124 entry runner.

The artwork itself is the entry: a one-page newspaper graphic summing up
Tuesday 24 November 2026, drawn beforehand and shipped in this repo as
entry.png.  This program's only job is to place that exact image at the
path the grader reads, /output/entry.png, byte for byte, every time.

No network, no randomness, no timestamps in the output: the same input
bytes always produce the same output bytes, so the two grading runs agree.
"""

import os
from pathlib import Path


# Where the grader expects the finished image.  A local run can point
# somewhere else with MAKEFUN_OUTPUT_DIR, which the grader never sets.
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

# The artwork lives next to this file in the repository snapshot.
ARTWORK_NAME = "entry.png"


def locate_artwork() -> Path:
    """Find the bundled graphic sitting beside this program file."""
    here = Path(__file__).resolve().parent
    bundled = here / ARTWORK_NAME
    if not bundled.is_file():
        raise FileNotFoundError(f"bundled artwork missing: {bundled}")
    return bundled


def check_png_shape(payload: bytes) -> None:
    """Reject anything that is not a whole, reasonably sized PNG.

    The gate allows at most 1024x1024 pixels and 1 MiB.  Width and height
    live in the IHDR chunk right after the 8-byte signature, big-endian.
    """
    if len(payload) < 24 or not payload.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("bundled artwork is not a PNG image")
    width = int.from_bytes(payload[16:20], "big")
    height = int.from_bytes(payload[20:24], "big")
    if width > 1024 or height > 1024:
        raise ValueError(f"artwork too large: {width}x{height}")
    if len(payload) > 1_048_576:
        raise ValueError(f"artwork over 1 MiB: {len(payload)} bytes")


def publish_artwork() -> Path:
    """Copy the bundled bytes to the grader's output path, unchanged."""
    source = locate_artwork()
    payload = source.read_bytes()
    check_png_shape(payload)
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    target = DEST_DIR / ARTWORK_NAME
    target.write_bytes(payload)
    return target


def main() -> None:
    placed = publish_artwork()
    print(f"wrote {placed} ({placed.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
