# stripunicode

Remove diacritics in Unicode text.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install stripunicode.

```bash
pip install git+https://gitlab.com/benjamineskola/stripunicode#egg=stripunicode
```

## Usage

```bash
$ stripunicode "Brontë"
Bronte
```

```python
from stripunicode import stripunicode

assert stripunicode("Brontë") == "Bronte"
```

## License

[ISC](https://choosealicense.com/licenses/isc/)
