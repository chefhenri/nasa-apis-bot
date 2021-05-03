import logging

from datetime import date

LOG_DIR = '/Users/henrylarson/PycharmProjects/nasa-apis-bot/logs'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s: - %(message)s'
DATEFMT = '%Y-%m-%d'


class BotLogger:
    def __init__(self, level=logging.INFO, log_dir=LOG_DIR):
        logging.basicConfig(level=level,
                            filename=f'{log_dir}/nasa-log-{date.today().strftime(DATEFMT)}.log',
                            filemode='a',
                            format=LOG_FORMAT)

    @staticmethod
    def log_info(msg):
        logging.info(msg)

    @staticmethod
    def log_warn(msg):
        logging.warning(msg)

    @staticmethod
    def log_err(msg):
        logging.error(msg)

    @staticmethod
    def log_debug(msg):
        logging.debug(msg)

    @staticmethod
    def log_crit(msg):
        logging.critical(msg)
