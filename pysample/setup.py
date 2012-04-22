# -*- coding: utf-8 -*-
try: import setuptools
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
from setuptools import setup, find_packages

setup(
    name = 'pysample',
    version = '0.1',
    packages = find_packages(),
)
