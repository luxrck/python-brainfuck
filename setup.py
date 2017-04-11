#!/usr/bin/env python
import brainfuck
from setuptools import setup


setup(name='brainfuck',
      version=brainfuck.__version__,
      description='Python Brainfuck Interpretor',
      author='lux.r.ck',
      author_email='lux.r.ck@gmail.com',
      packages=['brainfuck'],
      include_package_data=True,
      license="MIT License",
      zip_safe=False,
     )
