# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pathlib import Path

required = Path.cwd().joinpath("requirements.txt").read_text().splitlines()

setup(
    name='fast',
    version='0.3.0',
    description='The date api for TVH mail analysis',
    install_requires=required,
    packages=find_packages(exclude=('tests', 'docs')),
    python_requires=">=3.6"
)