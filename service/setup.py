#!/usr/bin/env python

import os
import sys
from codecs import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.txt'), 'r', 'utf-8') as handle:
    long_description = handle.read()

requires = [
    "alabaster==0.7.9",
    "amqp==2.1.1",
    "Babel==2.3.4",
    "cffi==1.9.1",
    "colorama==0.3.7",
    "cryptography==1.7.1",
    "docopt==0.6.2",
    "docutils==0.12",
    "ecdsa==0.13",
    "eventlet==0.19.0",
    "Fabric3==1.13.1.post1",
    "funcsigs==1.0.2",
    "futures==3.0.5",
    "gevent==1.1.2",
    "greenlet==0.4.10",
    "idna==2.1",
    "imagesize==0.7.1",
    "Jinja2==2.8",
    "kombu==4.0.0",
    "MarkupSafe==0.23",
    "mock==2.0.0",
    "mockredispy==2.9.3",
    "mocksqlalchemy==0.1.2",
    "mogo==0.4.0",
    "mongomock==3.7.0",
    "mysqlclient==1.3.9",
    "nameko==2.4.2",
    "nameko-sqlalchemy==0.0.4",
    "paramiko==1.17.2",
    "path.py==9.0",
    "pbr==1.10.0",
    "pluggy==0.4.0",
    "py==1.4.31",
    "pyasn1==0.1.9",
    "pycparser==2.17",
    "pycrypto==2.6.1",
    "Pygments==2.1.3",
    "pymongo==3.3.1",
    "PyMySQL==0.7.9",
    "pytest==3.0.4",
    "pytz==2016.7",
    "PyYAML==3.12",
    "redis==2.10.5",
    "requests==2.12.3",
    "sentinels==1.0.0",
    "six==1.10.0",
    "snowballstemmer==1.2.1",
    "Sphinx==1.5b1",
    "SQLAlchemy==1.1.4",
    "vine==1.1.3",
    "Werkzeug==0.11.11",
]

setup(
    name='service-platform',
    version='1.6',
    author='Eric.Zhou',
    author_email='xiaoxiang.cn@gmail.com',
    url='https://github.com/zhouxiaoxiang/platform',
    long_description=long_description,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    description='Cereson Platform.', )
