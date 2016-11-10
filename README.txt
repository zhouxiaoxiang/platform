PLATFORM README
====================

Written by Eric Zhou.
<xiaoxiang.cn@gmail.com>

Getting Started
-----------------

- Begin from here:
--./setup.py

-----------------
client:
```
from nameko.standalone.rpc import ClusterRpcProxy
with ClusterRpcProxy({"AMQP_URI":"amqp://guest:guest@localhost"}) as cli:
	result = cli.user_service.add(conn_id='10', user_name='', email="x@y", role='')
```

