import logging
import os

from datetime import date

LOG_FORMAT = '%(levelname)s:%(name)s:%(asctime)s - %(message)s'


class BotLogger:
    def __init__(self, log_dir):
        logging.basicConfig(filename=os.path.join(log_dir, f'{date.today()}-nasa-bot.log'),
                            filemode='w',
                            level=logging.DEBUG,
                            format=LOG_FORMAT)

    def log_info(self):
        pass

    def log_warn(self):
        pass

    def log_err(self):
        pass

    def log_debug(self):
        pass

    def log_crit(self):
        pass
