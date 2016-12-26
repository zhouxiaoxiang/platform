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

"""

import sys
import logging
from fabric.api import *
from os import path, walk


def _run(service):
    loc = "services"
    cmd = "nameko run"
    arg = "--config %s/services.cfg" % (
        path.dirname(path.abspath(__file__)))

    for fpath, _, fs in walk(loc):
        if (service + ".py") in fs:
            with lcd(fpath):
                local("%s %s %s" % (cmd, service, arg))
            break


def _test(test=None):
    loc = "tests"
    cmd = "py.test -v"
    arg = "test_%s.py"

    if test is None:
        local(cmd)
        return

    for fpath, _, fs in walk(loc):
        if (arg % test) in fs:
            with lcd(fpath):
                local(cmd)
            break


@task
@parallel
def doc():
    ''' Create project documents '''

    loc = "services"
    cmd = "sphinx-apidoc"
    arg = "docs"

    with settings(hide('running'), warn_only=True):
        local("%s -f -o %s services" % (cmd, arg))
        local("make html -C %s" % (arg))


@task
@parallel
def run(service):
    ''' Run some services, eg. user '''

    with settings(hide('running'), warn_only=True):
        _run(service)


@task
@parallel
def test(*args):
    ''' Run unit tests '''

    with settings(hide('running'), warn_only=True):
        if not args:
            _test()
        else:
            for test in args:
                _test(test)
