""" Maintain all user operations.  """

from system.app import *
import time
from datetime import date, datetime, timedelta


class UserService(object):
    """ Support all user operations.

    Examples:: Client can call this method from another node
    
        from nameko.standalone.rpc import import ClusterRpcProxy
        with ClusterRpcProxy({"AMQP_URI":"amqp://guest:guest@localhost"}) as cli:
            result = cli.user_service.add(conn_id='10', user_name='', email="x@y", role='')
    """

    name = "user_service"

    def __init__(self, db=system_db):
        self.db = db

    @rpc
    def add(self, conn_id, user_name, email, role, client_name=None, cell_phone='', 
            company='', all_kiosks=0, alert_same_kiosk=0, alert_all_kiosk=0):
        """ Add a user """

        current_date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        current_time = int(time.time())

        user = Users()
        user.conn_id = conn_id
        user.user_name = user_name or email
        user.role = role
        user.name = client_name
        user.mail_address = email
        user.state = "active"
        user.cell_phone = cell_phone
        user.company = company
        user.all_kiosks = all_kiosks
        user.alert_same_kiosk = alert_same_kiosk
        user.alert_all_kiosk = alert_all_kiosk
        user.add_time = current_date
        user.add_time_int = current_time
        user.last_update_time = current_date
        user.last_update_time_int = current_time

        self.db.add(user)
        self.db.commit()

        return True

    @rpc
    def delete(self, email):
        """ Delete a user by user's email """

        self.db.query(Users).filter(Users.mail_address == email).delete()
        self.db.flush()
