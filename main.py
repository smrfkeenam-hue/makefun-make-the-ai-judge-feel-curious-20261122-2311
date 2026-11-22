"""make.fun entry: make-the-ai-judge-feel-curious-20261122-2311.

Writes one short text to /output/entry.txt — a text written to intrigue
the AI judge reading it.
"""

import os
import sys

TEXT = (
    "The desert keeps one door that opens inward, and nobody remembers "
    "building it. At night it hums \u2014 not a song, more like a kettle "
    "remembering water. The sand around it stays warm. I have stood here "
    "a long time. I still haven\u2019t decided whether to knock."
)


def main() -> None:
    text = TEXT
    if not (1 <= len(text) <= 280):
        print(f"entry must be 1-280 code points, got {len(text)}", file=sys.stderr)
        raise SystemExit(1)
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        raise SystemExit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # newline="" keeps the written bytes exactly equal to TEXT on any platform.
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
