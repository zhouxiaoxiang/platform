#!/usr/bin/env python
# -*- coding: utf-8 -*-


from nameko.rpc import rpc, RpcProxy
from dao import *
from system.db import System_db

        
system_db = System_db().create_db()
