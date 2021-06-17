#!/usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

readme = open('README.rst').read()
history = open('CHANGES.rst').read().replace('.. :changelog:', '')

setup(
    name="python-mollusc",
    version='1.0.3',
    author="chowchow1",
    keywords = "python, clamav, antivirus, scanner, virus, libclamav, clamd",
    description = "Python clamd client (fork of python-clamd)",
    long_description=readme + '\n\n' + history,
    url="https://github.com/chowchow1/python-mollusc",
    package_dir={'': 'src'},
    packages=find_packages('src', exclude="tests"),
    classifiers = [
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
    ],
    zip_safe=True,
    include_package_data=False,
)
