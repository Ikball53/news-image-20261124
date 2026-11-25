#!/usr/bin/env python3
"""Publish the v2 front page for news-image-20261124.

Reads the finished 1024x1024 front page (entry.png, rendered by the local
build script with PIL so every glyph is crisp) and drops an exact copy into
the output directory the harness points at. Nothing is fetched, generated,
or randomised here: the image is a fixed asset and this program is only a
courier that checks the parcel before handing it over.
"""

import os
import struct
import sys
from pathlib import Path

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_EDGE = 1024
MAX_BYTES = 1024 * 1024


def read_asset() -> bytes:
    """Load the finished front page that sits next to this program."""
    here = Path(__file__).resolve().parent
    return (here / "entry.png").read_bytes()


def png_dimensions(blob: bytes) -> tuple[int, int]:
    """Pull width/height out of the IHDR chunk of a PNG byte string."""
    if blob[:8] != PNG_MAGIC:
        raise ValueError("entry.png does not start with the PNG signature")
    if len(blob) < 33 or blob[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


def check_parcel(blob: bytes) -> tuple[int, int]:
    """Reject anything that breaks the competition's image rules."""
    if len(blob) > MAX_BYTES:
        raise ValueError(
            "entry.png is %d bytes, over the 1 MiB limit" % len(blob))
    width, height = png_dimensions(blob)
    if width > MAX_EDGE or height > MAX_EDGE:
        raise ValueError(
            "entry.png is %dx%d, over the 1024x1024 limit"
            % (width, height))
    return width, height


def main() -> int:
    blob = read_asset()
    width, height = check_parcel(blob)
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(blob)
    echoed = target.read_bytes()
    if echoed != blob:
        raise ValueError("copy check failed: %s differs from entry.png"
                         % target)
    print("wrote %d bytes to %s (%dx%d PNG, copy verified)"
          % (len(blob), target, width, height))
    return 0


if __name__ == "__main__":
    sys.exit(main())
