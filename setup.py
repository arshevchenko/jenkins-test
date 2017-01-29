#!/usr/bin/env python

from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name="gdtesttask",
    version="1.0.1",
    packages=['gdtesttask'],
    description="Simple python project for jenkins task",
    long_description=long_description,
    url="https://github.com/shev2dev/jenkins-test",
    author="Shevchenko Artem",
    author_email="shevchenkoaa@sgu.ru",
    license="MIT",
    keywords="test jenkins easy"
)
