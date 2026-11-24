"""One Letter for Your Day — entry: Z (Z for zero sleep).

Writes exactly one character, "Z", to /output/entry.txt — no newline,
no extra whitespace. Deterministic. After writing, reads the file back
and validates it: content == "Z", length 1, UTF-8 round-trip, single line.
"""
import os

OUTPUT_PATH = "/output/entry.txt"
LETTER = "Z"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Validation: read back and assert the gate requirements.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    assert raw == b"Z", f"expected b'Z', got {raw!r}"
    assert len(raw) == 1, f"expected 1 byte, got {len(raw)}"
    text = raw.decode("utf-8")
    assert text == LETTER, f"expected 'Z', got {text!r}"
    assert len(text) == 1 and not text.isspace(), "must be exactly 1 non-whitespace char"
    assert text.encode("utf-8") == raw, "UTF-8 round-trip failed"
    assert "\n" not in text and "\r" not in text, "must be a single line with no newline"
    print("validated: /output/entry.txt is exactly b'Z' (1 byte)")


if __name__ == "__main__":
    main()
