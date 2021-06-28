from Logging.logging_setups import LogSetup

class App:

    def __init__(self):
        app_logger = LogSetup(self, file_log_level='WARNING', console_log_level='ERROR').logger
        app_logger.error('This will be logged on the console')
        app_logger.critical('This will be logged on the console')
        app_logger.warning('This will be logged inside the log files')
        app_logger.info('This will be logged inside the log files')

        app_logger = LogSetup(self).logger
        app_logger.error('This will be logged on the console')
        app_logger.critical('This will be logged on the console')
        app_logger.warning('This will be logged inside the log files')
        app_logger.info('This will be logged inside the log files')


if __name__ == '__main__':
    Appp = App()