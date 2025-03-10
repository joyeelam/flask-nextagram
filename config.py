import os

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or os.urandom(32)

    S3_BUCKET = os.environ.get('S3_BUCKET_NAME')
    S3_KEY = os.environ.get('S3_ACCESS_KEY')
    S3_SECRET = os.environ.get('S3_SECRET_ACCESS_KEY')
    S3_LOCATION = 'http://{}.s3.amazonaws.com/'.format(S3_BUCKET)

    MERCHANT_ID = os.environ.get('MERCHANT_ID')
    PUBLIC_KEY = os.environ.get('PUBLIC_KEY')
    PRIVATE_KEY = os.environ.get('PRIVATE_KEY')

    G_CLIENT_ID = os.environ.get("G_CLIENT_ID")
    G_CLIENT_SECRET = os.environ.get("G_CLIENT_SECRET")

    MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")

class ProductionConfig(Config):
    DEBUG = False
    ASSETS_DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    ASSETS_DEBUG = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ASSETS_DEBUG = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    ASSETS_DEBUG = True
