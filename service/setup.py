#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

with open('README.txt') as f:
    long_description = f.read()

with open('CHANGES.txt') as f:
    long_description += "\n\n" + f.read()

with open('requirements.txt') as f:
    requires = f.read()


setup(name='service-platform', 
      version='1.4',
      author='Eric.Zhou', 
      author_email='xiaoxiang.cn@gmail.com', 
      long_description=long_description,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      description='Cereson Platform.',
      )
