#!/usr/bin/env python

import ez_setup

ez_setup.use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "sell",
    version = "0.1",
    packages = find_packages(),
    license='MIT',
    long_description=open('README.md').read(),
    install_requires = ['pyserial'],
    extras_require = {
        'tests': ['nose >= 1.0']
    }
)