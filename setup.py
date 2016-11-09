#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

if len(sys.argv) < 2:
    usage = """
         _____ ______ _____  ______  _____  ____  _   _
        / ____|  ____|  __ \|  ____|/ ____|/ __ \| \ | |
       | |    | |__  | |__) | |__  | (___ | |  | |  \| |
       | |    |  __| |  _  /|  __|  \___ \| |  | | . ` |
       | |____| |____| | \ \| |____ ____) | |__| | |\  |
        \_____|______|_|  \_\______|_____/ \____/|_| \_|


     _____  _            _______ ______ ____  _____  __  __
    |  __ \| |        /\|__   __|  ____/ __ \|  __ \|  \/  |
    | |__) | |       /  \  | |  | |__ | |  | | |__) | \  / |
    |  ___/| |      / /\ \ | |  |  __|| |  | |  _  /| |\/| |
    | |    | |____ / ____ \| |  | |   | |__| | | \ \| |  | |
    |_|    |______/_/    \_\_|  |_|    \____/|_|  \_\_|  |_|

    Usage:

        ./setup.py develop        => install packages
        ./setup.py run [service]  => run some services, eg. user
        ./setup.py test           => run unit tests
        ./setup.py sys            => run tests under various enviroments
    """

    print(usage)
    sys.exit()


def extend(argv):
    def _extend(func):
        def __extend(*args, **kwargs):
            try:
                import extends
                extends.platform_extend(extends, argv)
            finally:
                pass

            return func(*args, **kwargs)
        return __extend
    return _extend


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
setup = extend(sys.argv[1:])(setup)

with open('requirements.txt') as f:
    requires = f.read().splitlines()

setup(
    name='platform',
    version='0.3',
    description='Cereson Platform.',
    long_description=README + '\n\n' + CHANGES,
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Platform",
        "Topic :: Internet :: HTTP",
    ],
    author='',
    author_email='',
    url='',
    keywords='platform',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points="""\
      """, )
