#! /usr/bin/env python3

from setuptools import find_packages, setup

setup(
    name="mipow",
    version="0.1",
    author="Josef Gajdusek",
    author_email="atx@atx.name",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mipow-ctl=mipow.tools.ctl:main"
        ]
    }
)
