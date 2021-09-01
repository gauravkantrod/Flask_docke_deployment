class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    ENV = 'production'


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345678'
    MYSQL_HOST = 'localhost'
    MYSQL_DB = 'coaching'
    MYSQL_PORT = 3306
    LOGGING_LEVEL = 'INFO'
    LOGFILE_PATH = 'logs/log.log'
    JWT_SECRET_KEY = '78d212ac-7f14-4918-b10f-b775f28db2c6'
    JWT_ACCESS_TOKEN_EXPIRES_TIME = 30
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    ENV = 'testing'
