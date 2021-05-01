import yaml
import logging
import logging.config


# LOG_FORMAT = '%(asctime)s:%(levelname)s:%(name)s: - %(message)s'
LOG_CFG = '/Users/henrylarson/PycharmProjects/nasa-apis-bot/logger_cfg.yml'


class BotLogger:
    def __init__(self):
        logging.config.dictConfig(yaml.load(open(LOG_CFG), Loader=yaml.FullLoader))
        self.logger = logging.getLogger(__name__)

    def log_info(self, msg):
        self.logger.info(msg)

    def log_warn(self):
        pass

    def log_err(self):
        pass

    def log_debug(self):
        pass

    def log_crit(self):
        pass
