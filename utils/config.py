from dotenv import dotenv_values


def get_config(env_path):
    return dotenv_values(env_path)
