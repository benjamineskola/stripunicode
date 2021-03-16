# Always prefer setuptools over distutils
import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="stripunicode",
    version="0.0.1",
    description="Remove diacritics in Unicode text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/benjamineskola/stripunicode",
    author="Benjamin Eskola",
    author_email="ben@eskola.uk",
    license="ISC license",
    classifiers=["License :: OSI Approved :: ISC License (ISCL)"],
    packages=find_packages(),
    python_requires=">=3.5, <4",
    install_requires=[],
    entry_points={"console_scripts": ["stripunicode=stripunicode:main"]},
    project_urls={
        "Bug Reports": "https://gitlab.com/benjamineskola/stripunicode/issues",
        "Source": "https://gitlab.com/benjamineskola/stripunicode/",
    },
)