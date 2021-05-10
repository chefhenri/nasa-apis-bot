import unittest

from apod.client import ApodClient
from utils.config import get_cfg
from utils.logger import BotLogger


class TestClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls._config = get_cfg('../../.env')
        cls._logger = BotLogger(log_lvl=cls._config['TEST_LOG_LVL'], log_dir=cls._config['TEST_LOG_DIR'])
        cls._client = ApodClient(config=cls._config, logger=cls._logger)
