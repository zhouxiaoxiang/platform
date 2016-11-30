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

import os
import sys
from fabric.api import *


def _run(service):
    loc, cmd, arg = "services", "nameko run", "--broker amqp://guest:guest@localhost"
    for path, _, fs in os.walk(loc):
        if (service + ".py") in fs:
            with lcd(path):
                local("%s %s %s" % (cmd, service, arg))
            break


def _test(test=None):
    loc, cmd, arg = "tests", "py.test", "test_%s.py"
    if test is None:
        local('%s' % (cmd))
        return

    for path, _, fs in os.walk(loc):
        if (arg % test) in fs:
            with lcd(path):
                local(cmd)
            break


def doc():
    ''' Create project documents '''

    loc, cmd, arg = "services", "sphinx-apidoc", "docs"
    local("%s -f -o %s services" % (cmd, arg))
    local("make html -C %s" % (arg))


def sys():
    ''' Run tests with full new python environment '''

    cmd = "tox"
    local(cmd)


def run(*args):
    ''' Run some services, eg. user '''

    for service in args:
        from multiprocessing import Process
        Process(target=_run, args=(service, )).start()


def test(*args):
    ''' Run unit tests '''

    if not args:
        _test()
    else:
        for test in args:
            _test(test)
