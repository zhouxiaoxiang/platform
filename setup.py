#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
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
        ./setup.py develop         => install packages     
        ./setup.py doc             => create project documents
        ./setup.py run [service]   => run some services, eg. user
        ./setup.py test            => run unit tests
        ./setup.py sys             => run python system tests
"""

import sys
from setuptools import setup


version = {"name": 'platform',
           "version": '0.5',
           "description": 'Cereson Platform.',
           }


cmd = sys.argv[1:]
if not cmd:
    print(__doc__)
    sys.exit()


def platform_extend(argv):
    import extends
    extends.platform_extend(extends, argv)

    def _extend(func):
        def __extend(**attrs):

            from setuptools import find_packages

            with open('README.txt') as f:
                long_description = f.read()

            with open('CHANGES.txt') as f:
                long_description += "\n\n" + f.read()

            with open('requirements.txt') as f:
                attrs["install_requires"] = f.read()

            attrs["long_description"] = long_description
            attrs["packages"] = find_packages()
            attrs["include_package_data"] = True
            attrs["zip_safe"] = False

            return func(**attrs)
        return __extend
    return _extend


platform_extend(cmd)(setup)(**version)
