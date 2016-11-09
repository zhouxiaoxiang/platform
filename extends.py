#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys


def run_service(service):
    loc = "services"
    cmd = "nameko run"
    arg = "--broker amqp://guest:guest@localhost"

    for path, _, fs in os.walk(loc):
        if (service + ".py") in fs:
            os.system("cd %s; %s %s %s" % (path, cmd, service, arg))
            break


def platform_run(services):
    for service in services:
        from multiprocessing import Process
        Process(target=run_service, args=(service, )).start()


def platform_test(tests):
    loc = "tests"
    cmd = "py.test"
    fmt = "test_%s.py"

    if len(tests) < 1:
        os.system('%s' % (cmd))
        return

    for test in tests:
        for path, _, fs in os.walk(loc):
            if (fmt % test) in fs:
                os.system("cd %s; %s" % (path, cmd))
                break


def platform_sys(argv):
    cmd = "tox"
    os.system('%s %s' % (cmd, " ".join(argv)))


def platform_extend(extends, argv):
    fmt = "platform_%s"
    cmd = fmt % (argv[0])

    if hasattr(extends, cmd):
        getattr(extends, cmd)(argv[1:])
        sys.exit()
