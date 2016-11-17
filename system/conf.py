import ConfigParser
from os import path, pardir


class System_config(object):

    """
    Supply system configuration

    Example
    -------
    Get system configuration

    >>> from system.conf import System_config
    >>> config = System_config().get()
    >>> database = config.get("system", "database")
    """

    CONFIG = "platform.ini"

    def __init__(self):

        self.config = None

    def get(self):
        """ Return ConfigParser result """

        current_dir = path.dirname(path.abspath(__file__))
        config_path = path.abspath(path.join(current_dir,
                                   pardir, self.CONFIG))
        self.config = ConfigParser.ConfigParser()
        with open(config_path) as f:
            self.config.readfp(f)

        return self.config
