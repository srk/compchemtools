# -*- coding: utf-8 -*-
"""setup.py: setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('xyz_to_xyz/xyz_to_xyz.py').read(),
    re.M
    ).group(1)

setup(
    name = "xyz_to_xyz",
    packages = ["xyz_to_xyz"],
    entry_points = {
        "console_scripts": ['xyz_to_xyz=xyz_to_xyz.xyz_to_xyz:main',]
        },
    version = version,
    author='Prof. Steven R. Kirk',
    author_email='stevenrkirk@gmail.com',
    description = "xyz_to_xyz",
    url = 'https://www.beaconresearch.org'
    )