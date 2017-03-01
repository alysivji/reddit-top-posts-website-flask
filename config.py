## MongoEngine Note: include db name in URI; it overwrites all others

class Config(object):
    MONGODB_HOST = 'mongodb://localhost:27017/sivji-sandbox'
    DEBUG = False
    TESTING = True

class ProductionConfig(Config):
    MONGODB_HOST = 'mongodb://localhost:27017/sivji-sandbox'

class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_HOST = 'mongodb://localhost:27017/sivji-sandbox'

class TestingConfig(Config):
    TESTING = True
