# FIXME: Fix imports
import os
import unittest

from utils.logging import LOG_FILE, init_logger, get_logger, wrap, entering, exiting

LOG_LVL = 'logging.DEBUG'
LOG_DIR = '../../logs'

FUNC_NO_RETURN = 'The function did not return the expected result.'
MSG_NOT_LOGGED = 'The log filesize has not increased, the message was not logged.'


def get_log_filesize():
    """ Gets the size of the log file """
    return os.path.getsize(f"{LOG_DIR}/{LOG_FILE}")


@wrap(entering, exiting)
def wrapped_func():
    """ A function wrapped for testing """
    return 'I was wrapped!'


# FIXME: Update unit tests
class LoggerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # TODO: Init logger
        init_logger(log_lvl=LOG_LVL, log_dir=LOG_DIR)

        cls._logger = get_logger()
        cls._filesize = get_log_filesize()

    def setUp(self) -> None:
        self.log_file_size = get_log_filesize()

    def test_info(self):
        self._logger.info('Test info message')
        self.assertTrue(self.log_file_size < get_log_filesize(), MSG_NOT_LOGGED)

    def test_debug(self):
        self._logger.debug('Test info message')
        self.assertTrue(self.log_file_size < get_log_filesize(), MSG_NOT_LOGGED)

    def test_wrap(self):
        test_res = wrapped_func()

        self.assertIsNotNone(test_res, FUNC_NO_RETURN)
        self.assertTrue(self.log_file_size < get_log_filesize(), MSG_NOT_LOGGED)
