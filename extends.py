import os
import sys


def _run(service):
    loc = "services"
    cmd = "nameko run"
    arg = "--broker amqp://guest:guest@localhost"

    for path, _, fs in os.walk(loc):
        if (service + ".py") in fs:
            os.system("cd %s; %s %s %s" % (path, cmd, service, arg))
            break


def _test(test=None):
    loc = "tests"
    cmd = "py.test"
    fmt = "test_%s.py"

    if test is None:
        os.system('%s' % (cmd))
        return

    for path, _, fs in os.walk(loc):
        if (fmt % test) in fs:
            os.system("cd %s; %s" % (path, cmd))
            break


def _sys(arg):
    cmd = "tox"
    os.system('%s %s' % (cmd, arg))


def platform_run(services):
    for service in services:
        from multiprocessing import Process
        Process(target=_run, args=(service, )).start()


def platform_test(tests):
    if not tests:
        _test()
    else:
        for test in tests:
            _test(test)


def platform_sys(arg):
    _sys(" ".join(arg))


def platform_extend(extends, argv):
    fmt = "platform_%s"
    cmd = fmt % (argv[0])

    if hasattr(extends, cmd):
        getattr(extends, cmd)(argv[1:])
        sys.exit()
