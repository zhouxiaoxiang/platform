import mogo
from datetime import datetime as dt

from oriole.app import *
from oriole.log import Log


class UserEventLogService(App):

    """
    Support all syslog.

    >>> from nameko.standalone.rpc import ClusterRpcProxy
    >>> CONFIG = {"AMQP_URI":"amqp://guest:guest@localhost"}
    >>> with ClusterRpcProxy(CONFIG) as services:
    >>>     result = services.user_event_log_service.add_log({"content": "info"})
    """

    name = "user_event_log_service"

    def __init__(self):
        super(UserEventLogService, self).init()
        self.log = Log("userEventLog").get()

    @rpc
    def add_log(self, content):
        """ Add a log. """

        content["time"] = dt.now()
        print('add_log: {}'.format(content))
        for k, v in content.items():
            print(u'{0:>30}: {1}'.format(k, v))
        print('-'*80)

        result = self.log.insert_one(content)
        return result.acknowledged

    @rpc
    def get_log(self, query):
        """ Get logs. """

        keys_tobe_delete = ["get_count", "sort_key", "sort_order", "limit", "offset", "start_date", "end_date"]
        action_level_permission = {
            "master": ["master", "host", "client"],
            "host": ["host", "client"],
            "client": ["client"]
        }
        # filter empty value
        query = dict((k, v) for k, v in query.items() if v)
        print('get_log: %s' % query)

        start_date = query.get("start_date")
        end_date = query.get("end_date")
        action_level = query.get("action_level")
        support_account = query.get("support_account")

        try:
            start_date = dt.strptime(start_date, "%Y-%m-%d %H:%M:%S")
            end_date = dt.strptime(end_date, "%Y-%m-%d %H:%M:%S")
        except (ValueError, TypeError):
            start_date = None
            end_date = None

        if start_date and end_date:
            query["time"] = {"$gte": start_date, "$lt": end_date}

        if action_level and (action_level in action_level_permission):
            query["action_level"] = {"$in": action_level_permission[action_level]}
        if support_account:
            query["support_account"] = {"$nin": support_account}

        if query.get("get_count"):
            for k in keys_tobe_delete:
                if query.get(k):
                    del query[k]
            return self.log.find(query).count()

        limit = query.get("limit")
        offset = query.get("offset")
        sort_key = query.get("sort_key")
        sort_order = query.get("sort_order", "")

        for k in keys_tobe_delete:
            if query.get(k):
                del query[k]

        cursor_res = self.log.find(query)

        if sort_key:
            if sort_order.lower().startswith("des"):
                cursor_res = cursor_res.sort(sort_key, mogo.DESC)
            else:
                cursor_res = cursor_res.sort(sort_key, mogo.ASC)

        if offset:
            cursor_res = cursor_res.skip(offset)
        if limit:
            cursor_res = cursor_res.limit(limit)

        result = []
        for r in cursor_res:
            r['id'] = str(r['_id'])
            del r['_id']
            result.append(r)

        return result
