import sys
import unicodedata
from typing import Optional


def stripunicode(
    text: str, retain_missing: bool = True, substitute: Optional[str] = None
) -> str:
    """Return an ASCII approximation of the input text

    Keyword arguments:
    - `retain_missing`: if True, pass through unrecognised characters unchanged; if False, delete them from the output.
    - `substitute`: if set to a non-empty string, unrecognised characters will be replaced by this in the output.
    """
    retval = ""
    for char in text:
        val = ord(char)
        if val in range(9, 14) or val in range(32, 127):
            retval += char
        elif val in [0x2013, 0x2014]:
            # en-dash | em-dash -> hyphen
            retval += "-"
        elif val in range(0x0080, 0x02FF + 1) or val in range(0x1D00, 0x1EFF + 1):
            # Latin-1 Supplement, Latin Extended-A, Latin Extended B, IPA Extensions, Spacing Modifier Letters
            # Phonetic Extensions, Phonetic Extensions Supplement, Latin Extended Additional
            if decomposition := unicodedata.decomposition(char).split():
                while decomposition and decomposition[0].startswith("<"):
                    del decomposition[0]
                for i in decomposition:
                    new_val = int(i, 16)
                    if new_val > 127:
                        retval += stripunicode(chr(new_val), False)
                    else:
                        retval += chr(new_val)
            elif retain_missing or substitute:
                retval += substitute or char
        elif retain_missing or substitute:
            retval += substitute or char
    return retval


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(stripunicode(" ".join(sys.argv[1:])))
    else:
        print(stripunicode(sys.stdin.read()))
