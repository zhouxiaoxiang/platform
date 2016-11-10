#!/usr/bin/env python
# -*- coding: utf-8 -*-


from nameko.rpc import rpc, RpcProxy
from dao import *
from system.db import DB

        
db = DB().create_db()
