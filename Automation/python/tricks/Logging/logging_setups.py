import logging


class LogSetup:
    def __init__(self, level):
        level = level if level else 'INFO'
        logging.basicConfig(level=level)
        self.logger = logging.getLogger(type(self).__name__)

