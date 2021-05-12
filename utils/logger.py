import logging

from datetime import date

from utils.config import get_root_cfg

DATEFMT = '%Y-%m-%d'
LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s: - %(message)s'


class BotLogger:
    def __init__(self):
        self._config = get_root_cfg()
        logging.basicConfig(level=eval(self._config['log_lvl']),
                            filename=f"{self._config['log_dir']}/nasa-log-{date.today().strftime(DATEFMT)}.log",
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
