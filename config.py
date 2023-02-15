class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    OPENAI_KEY = "api_key"


config = {
    'development': DevelopmentConfig,
}
