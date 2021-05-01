from dotenv import dotenv_values


def load_config():
    return dotenv_values('/Users/henrylarson/PycharmProjects/nasa-apis-bot/.env')
