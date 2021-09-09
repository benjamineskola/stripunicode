import pathlib
import sys

import pytest

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent.absolute()))

from stripunicode import stripunicode


def test_bronte():
    assert stripunicode("Brontë") == "Bronte"


def test_cyrillic_passthrough():
    assert stripunicode("Достоевский") == "Достоевский"


def test_cyrillic_noretain():
    assert stripunicode("Достоевский", retain_missing=False) == ""


def test_cyrillic_substitute():
    assert stripunicode("Достоевский", substitute="?") == "???????????"


def test_digraph():
    assert stripunicode("Ĳ") == "IJ"
    assert stripunicode("ĳ") == "ij"


def test_digraph2():
    assert stripunicode("Ǆ") == "DZ"
    assert stripunicode("ǅ") == "Dz"
    assert stripunicode("ǆ") == "dz"
    assert stripunicode("Ǳ") == "DZ"
    assert stripunicode("ǲ") == "Dz"
    assert stripunicode("ǳ") == "dz"


def test_dashes():
    assert stripunicode("–") == "-"
    assert stripunicode("—") == "-"


def test_icelandic():
    assert stripunicode("Ðð") == "Dd"
    assert stripunicode("Þþ") == "THth"
