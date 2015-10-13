# -*- coding: utf-8 -*-
import os
import io
import re
from setuptools import (
    setup,
    find_packages,
    )


def here(path):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)


def read(*names, **kwargs):
    with io.open(os.path.join(os.path.dirname(__file__), *names),
                 encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='configram',
    version=find_version('src/configram/version.py'),
    description='Generic application configurator like pyramid style',
    long_description=open(here('README.rst', encoding='utf8')).read(),
    packages=find_packages(exclude=['tests*']),
    install_requires=[
        'six',
        'zope.interface',
        'zope.component',
        'zope.dottedname',
        ],
    )
