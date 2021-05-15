# FIXME: Fix imports
import os
import unittest

from datetime import date

from utils.config import init_root_cfg, get_logger_cfg
from utils.logger import BotLogger

ENV_PATH = '/Users/henrylarson/PycharmProjects/nasa-apis-bot/.env.dev'


# FIXME: Fix constructors
class LoggerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        init_root_cfg(ENV_PATH)
        cls._config = get_logger_cfg()
        cls._logger = BotLogger()
        cls._filename = f"nasa-log-{date.today().strftime('%Y-%m-%d')}.log"
        cls._filesize = os.path.getsize(f"{cls._config['log_dir']}/{cls._filename}")

    def setUp(self) -> None:
        self.log_file_size = self.get_log_filesize()

    def get_log_filesize(self):
        return os.path.getsize(f"{self._config['log_dir']}/{self._filename}")

    def test_log_info(self):
        self._logger.info('Test info message')
        self.assertTrue(self.get_log_filesize() > self._filesize)

    def test_log_warn(self):
        self._logger.warn('Test warning message')
        self.assertTrue(self.get_log_filesize() > self._filesize)

    def test_log_err(self):
        self._logger.err('Test error message')
        self.assertTrue(self.get_log_filesize() > self._filesize)

    def test_log_debug(self):
        self._logger.debug('Test debug message')
        self.assertTrue(self.get_log_filesize() > self._filesize)

    def test_log_crit(self):
        self._logger.crit('Test critical message')
        self.assertTrue(self.get_log_filesize() > self._filesize)
