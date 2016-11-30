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
from system.conf import Config
from multiprocessing import Process


def _conf(task=None):
    if task:
        config = Config(config="platform.cfg")
        return config[task]


def _run(service):
    loc, cmd, arg = _conf('run')
    prefix = "--broker amqp://"

    for path, _, fs in os.walk(loc):
        if (service + ".py") in fs:
            with lcd(path):
                local("%s %s %s" % (cmd, service,
                                    prefix + arg))
            break


def _test(test=None):
    loc, cmd, arg = _conf('test')

    if test is None:
        local(cmd)
        return

    for path, _, fs in os.walk(loc):
        if (arg % test) in fs:
            with lcd(path):
                local(cmd)
            break


@task
def doc():
    ''' Create project documents '''

    loc, cmd, arg = _conf('doc')
    local("%s -f -o %s services" % (cmd, arg))
    local("make html -C %s" % (arg))


@task
def sys():
    ''' Run tests with full new python environment '''

    loc, cmd, arg = _conf('sys')
    local(cmd)


@task
def run(*args):
    ''' Run some services, eg. user '''

    for service in args:
        Process(target=_run, args=(service, )).start()


@task
def test(*args):
    ''' Run unit tests '''

    if not args:
        _test()
    else:
        for test in args:
            _test(test)
