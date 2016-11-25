from services.user.user import *
from system.test import *


def aaa(*args):
    print 
    print "<<<<<<<<<<<<<", args
    print 
    return(args)

def test_service(service):
    
    aa = UserService()
    #aa.db.add.return_value = "XXXXXXXXXXXXXXXXXXXxx"
    aa.db.add = MagicMock(side_effect=aaa)
    #aa.db.commit = MagicMock(side_effect=aaa)
    aa.add_user(conn_id='9', user_name='', email="x@y", role='')

    print(">>>>>>>>>>>", aa.db.add.return_value)
