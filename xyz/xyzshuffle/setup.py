# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('xyzshuffle/xyzshuffle.py').read(),
    re.M
    ).group(1)

setup(
    name = "xyzshuffle",
    packages = ["xyzshuffle"],
    entry_points = {
        "console_scripts": ['xyzshuffle=xyzshuffle.xyzshuffle:main',]
        },
    version = version,
    author='Prof. Steven R. Kirk',
    author_email='stevenrkirk@gmail.com',
    description = "xyzshuffle",
    url = 'https://www.beaconresearch.org',
    install_requires=[],
    )
