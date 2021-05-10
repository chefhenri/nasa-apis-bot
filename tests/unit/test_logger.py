import os
import unittest

from datetime import date

from utils.logger import BotLogger


class LoggerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._logger = BotLogger('logging.DEBUG', '../../logs')
        cls._filename = f'nasa-log-{date.today().strftime("%Y-%m-%d")}.log'
        cls._filesize = os.path.getsize(f'../../logs/{cls._filename}')

    def setUp(self) -> None:
        self.log_file_size = self.get_log_filesize()

    def get_log_filesize(self):
        return os.path.getsize(f'../../logs/{self._filename}')

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
