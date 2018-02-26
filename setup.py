"""
Setup for BitPanda Logger
"""

import os
from setuptools import setup

def read(fname):
    """
    Helper to read README
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

setup(
    name='eth44',
    version=read('VERSION'),
    author='Danny McDonald',
    author_email='daniel.mcdonald@bitpanda.com',
    description=('Ethereum derivation'),
    keywords='bitpanda utilities',
    packages=['eth44', 'tests'],
    long_description=read('README.md'),
    install_requires=['two1', 'pycrypto', 'rlp', 'pycryptodome'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
    ],
)
