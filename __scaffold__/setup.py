#!/usr/bin/python3

from setuptools import setup
from setuptools import find_packages

with open("readme.md", "r") as fh:
    readme = fh.read()

setup(
    name="something",
    version="0.0.1",
    author="someone",
    author_email="something@gmail.com",
    description="something",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/user/repository",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'utility = __dir__.file:app',
        ],
    },
    install_requires=[
        'numpy<=1.23.0',
        'pandas<=2.0.2',
        'bs4<=0.0.1',
        'matplotlib<=3.3.0'
        'requests<=2.28.1'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX",
    ],
)