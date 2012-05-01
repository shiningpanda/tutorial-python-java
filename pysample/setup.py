# -*- coding: utf-8 -*-
import os
import time
import codecs
try: import setuptools
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()
from setuptools import setup, find_packages
# Folder containing the setup.py
root = os.path.dirname(os.path.abspath(__file__))
# Path to __version__ module
version_file = os.path.join(root, 'pysample', '__version__.py')
# Check if this is a source distribution.
# If not create the __version__ module containing the version
if not os.path.exists(os.path.join(root, 'PKG-INFO')):
    timestamp = int(os.getenv('TIMESTAMP', time.time() * 1000)) / 1000
    fd = codecs.open(version_file, 'w', 'utf-8')
    fd.write('version   = %r\n' % os.getenv('VERSION', '?').replace('-SNAPSHOT', '.dev-%d' % timestamp))
    fd.write('revision  = %r\n' % os.getenv('BUILD_NUMBER', '?'))
    fd.write('timestamp = %d\n' % timestamp)
    fd.close()
# Load version
exec(open(version_file).read())
# Setup
setup(
    name = 'pysample',
    version = version,
    packages = find_packages(),
    setup_requires = [
        'nose >= 1.0',
    ]
)
