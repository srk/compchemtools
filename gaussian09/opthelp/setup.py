# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('opthelp/opthelp.py').read(),
    re.M
    ).group(1)

setup(
    name = "opthelp",
    packages = ["opthelp"],
    entry_points = {
        "console_scripts": ['opthelp=opthelp.opthelp:main',]
        },
    version = version,
    author='Prof. Steven R. Kirk',
    author_email='stevenrkirk@gmail.com',
    description = "Find the current best structure in a Gaussian 09 geometry optimization run, then create a new input file starting from that geometry.",
    url = 'https://www.beaconresearch.org',
    install_requires=[],
    )
