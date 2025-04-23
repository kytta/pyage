"""Packaging logic for age."""
import os
import sys

from setuptools import setup

import versioneer


# add the src directory to PYTHONPATH so we can import the version
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))  # noqa

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)
