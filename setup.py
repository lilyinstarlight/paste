#!/usr/bin/env python3
from distutils.core import setup

from paste import name, version


setup(
    name=name,
    version=version,
    description='a web service for storing pastes that only last for a short period of time',
    license='MIT',
    author='Foster McLane',
    author_email='fkmclane@gmail.com',
    packages=['paste'],
    package_data={'paste': ['html/*.*']},
)
