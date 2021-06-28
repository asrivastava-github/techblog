import logging


class LogSetup:
    def __init__(self, className, level=None, file_log_level=None, console_log_level=None):
        log_file = 'app.log'
        level = level if level else 'INFO'
        self.logger = logging.getLogger('{}'.format(type(className).__name__))
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        # self.logger.setLevel(level=level)

        # create file handler with desired logging level
        fh_level = file_log_level if file_log_level else level
        file_handler = logging.FileHandler(filename=log_file)
        file_handler.setLevel(level=fh_level)

        # create console handler to print the logs on console
        ch_level = console_log_level if console_log_level else level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level=ch_level)

        # Attach formatter to log handlers
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # add the handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)


