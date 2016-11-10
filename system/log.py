#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mogo
import logging
from mongolog.handlers import MongoHandler


""" This module will specify db url, return a log handler. """


class Log(object):
    host = "localhost"
    db = None
    tb = None
    """ Establish a connection to db. """

    def __init__(self, module="test"):
        self.conn = mogo.connect(self.host)
        self.log = self.conn[self.db][self.tb]
        self.module = module

    """ Return log handler 

    Use collection, althrough knowledge about mongodb is required.
    """

    def get(self):
        return self.log


''' Create specific log handler '''


class SysLog(Log):
    db = "sysLog"
    tb = "log"

    def __init__(self, module="test"):
        self.log = logging.getLogger(module)
        self.log.setLevel(logging.DEBUG)
        self.log.addHandler(MongoHandler.to(self.tb, self.db, self.host))

    def get(self):
        return self.log


''' These log types is due to various applications.'''


class SysEventLog(Log):
    db = "eventLog"
    tb = "sys"

    def __init__(self,  module="test"):
        super(SysEventLog, self).__init__()


class UserEventLog(Log):
    db = "eventLog"
    tb = "user"

    def __init__(self,  module="test"):
        super(UserEventLog, self).__init__()


class StockEventLog(Log):
    db = "eventLog"
    tb = "stock"

    def __init__(self,  module="test"):
        super(StockEventLog, self).__init__()


class NopickedEventLog(Log):
    db = "eventLog"
    tb = "nopicked"

    def __init__(self,  module="test"):
        super(NopickedEventLog, self).__init__()

