import logging

from datetime import date

# LOG_DIR = '../logs'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s: - %(message)s'
DATEFMT = '%Y-%m-%d'


class BotLogger:
    def __init__(self, log_lvl, log_dir):
        logging.basicConfig(level=eval(log_lvl),
                            filename=f'{log_dir}/nasa-log-{date.today().strftime(DATEFMT)}.log',
                            filemode='a',
                            format=LOG_FORMAT)

    @staticmethod
    def info(msg):
        logging.info(msg)

    @staticmethod
    def warn(msg):
        logging.warning(msg)

    @staticmethod
    def err(msg):
        logging.error(msg)

    @staticmethod
    def debug(msg):
        logging.debug(msg)

    @staticmethod
    def crit(msg):
        logging.critical(msg)
