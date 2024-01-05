#!/usr/bin/env python3

"""
d2lfg setup
===========

This file contains setup for the Diablo 2 Loot Filter Generator (d2lfg).
"""

from pathlib import Path

from setuptools import setup

thisdir = Path(__file__).cwd()

with open(thisdir / "README.rst", "r") as f:
    readme = f.read()

source_url = "https://www.github.com/jkoelndorfer/d2lfg"

if __name__ == "__main__":
    setup(
        name="d2lfg",
        setup_requires=["setuptools_scm"],
        use_scm_version=True,
        description="Diablo 2 Loot Filter Generator (d2lfg)",
        long_description=readme,
        long_description_content_type="text/x-rst",
        author="John Koelndorfer",
        author_email="d2lfg@johnk.io",
        url=source_url,
        include_package_data=True,
        package_data={"": ["LICENSE", "py.typed", "README.rst"]},
        package_dir={"": "src"},
        python_requires=">=3.8.0",
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            "Natural Language :: English",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "Programming Language :: Python :: 3.12",
            "Topic :: Games/Entertainment",
            "Topic :: Software Development :: Libraries",
        ],
        project_urls={
            "Source": source_url,
        },
    )
