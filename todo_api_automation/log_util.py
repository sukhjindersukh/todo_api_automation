import logging
from pathlib2 import Path

class Log_Util:

    logger =logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    path =Path('.').absolute().parent / 'app.log'
    fh = logging.FileHandler(str(path))
    fh.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    def info(self,message):
        Log_Util.logger.info(message)

    def warn(self, message):
        Log_Util.logger.warn(message)
