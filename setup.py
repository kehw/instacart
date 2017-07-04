from setuptools import setup, find_packages

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os
import re
import sys

import instacart

here = os.path.abspath(os.path.dirname(__file__))



def find_version(*file_paths):
# Open in Latin-1 so that we avoid encoding errors.
# Use codecs.open for Python 2 compatibility
    with codecs.open(os.path.join(here, *file_paths), 'r', 'latin1') as f:
    version_file = f.read()
    # The version line must have the form __version__ = 'ver'
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


# Get the long description from the relevant file
with codecs.open('README.rst', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'instacart',
    version=instacart.__version__
)
