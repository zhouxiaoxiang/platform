import os
import ConfigParser


class System_config(object):
    ''' Get system config handler 
    Example::
    --------
    from system import System_config
    config = System_config().get
    config.get("", "")
    '''

    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.abspath(os.path.join(current_dir,
                                                   os.pardir,
                                                   "platform.ini"))
        self.config = ConfigParser.ConfigParser()
        with open(config_path) as f:
            self.config.readfp(f)

    def get(self):
        ''' Get config handler '''
        return self.config
