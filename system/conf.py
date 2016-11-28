import yaml
from os import path, pardir


class Config(object):

    """
    Supply system configuration

    Examples
    --------
    Get system configuration

    >>> from system.conf import Config
    >>> config = Config()
    >>> database = config["database"]
    >>> "mysql" in database
    True
    """

    FILE = "platform.cfg"
    __obj = ""

    def __new__(self, *args, **kwargs):
        """ Return ConfigParser """
        
        if not self.__obj:
            curdir = path.dirname(path.abspath(__file__))
            config = path.join(curdir, pardir, self.FILE)
            with open(path.abspath(config)) as f:
                self.__obj = yaml.load(f)

        return self.__obj

if __name__ == "__main__":
    import doctest
    doctest.testmod()
