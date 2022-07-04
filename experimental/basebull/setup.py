"""
Basebull.

Packaging for basebull
https://github.com/jrebe/basebull
Adapted from: https://github.com/pypa/sampleproject/blob/master/setup.py
"""

from io import open
from os import path

from setuptools import find_packages, setup


HERE = path.abspath(path.dirname(__file__))


with open(path.join(HERE, "README.md"), encoding="utf-8") as f:
    LONG_DESCRIPTION = f.read()

with open(path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    INSTALL_REQUIRES = f.read().splitlines()

setup(
    name="basebull",
    version="0.1.15",
    description="baseball park optimization problem solver",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/jrebe/basebull",
    author="jrebe",
    author_email="jrebe@users.noreply.github.com",
    packages=find_packages(exclude=["contrib", "docs", "test"]),
    package_data={"myapp": ["basebull/data/*.csv"]},
    include_package_data=True,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    install_requires=INSTALL_REQUIRES,
    tests_require=["pytest"],
)
