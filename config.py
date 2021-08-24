class Config(object):
    DEBUG = False
    TESTING = False
    # DATABASE_URI = 'sqlite://:memory:'


class ProductionConfig(Config):
    # SECRET_KEY = "98d0s809SD990AS)(dS&A&*d78(*&ASD08A"
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    ENV = "development"


class TestingConfig(Config):
    TESTING = True
