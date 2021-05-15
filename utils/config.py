import functools

from dotenv import dotenv_values

root_config = {}


def init_root_cfg(env_path):
    """ Initializes the root config from the .env file """
    global root_config
    root_config = dotenv_values(dotenv_path=env_path)


@functools.lru_cache(maxsize=None)
def get_logger_cfg():
    """ Gets the root logger config and caches it """
    return {
        'log_lvl': root_config['LOG_LVL'],
        'log_dir': root_config['LOG_DIR']
    }


@functools.lru_cache(maxsize=None)
def get_client_cfg():
    """ Gets the API wrapper client config and caches it """
    return {
        'token': root_config['BOT_TOKEN'],
        'endpoint': root_config['APOD_GQL_ENDPOINT'],
        'api_key': root_config['APOD_API_KEY']
    }


@functools.lru_cache(maxsize=None)
def get_hook_cfg():
    """ Gets the webhook object config and caches it """
    return {
        'url': root_config['WEBHOOK_URL']
    }
