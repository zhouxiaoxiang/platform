import ConfigParser
from os import path, pardir


class System_config(object):

    """
    Supply system configuration

    Examples
    --------
    Get system configuration

    >>> from system.conf import System_config
    >>> config = System_config()
    >>> database = config.get("system", "database")
    """

    FILE = "platform.ini"
    _obj = ""

    def __new__(cls, *args, **kwargs):
        """ Return ConfigParser """

        if not cls._obj:
            curdir = path.dirname(path.abspath(__file__))
            config = path.join(curdir, pardir, cls.FILE)
            cls._obj = ConfigParser.ConfigParser()
            with open(path.abspath(config)) as f:
                cls._obj.readfp(f)

        return cls._obj
