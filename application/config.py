import os
import binascii

class Config(Object):
    """Base config"""
    DEBUG = False
    PORT = 8080
    SECRET_KEY = binascii.hexlify(os.urandom(4096)).decode()
    SESSION_LIFETIME = 60*60 # 1h


class ProductionConfig(Config):
    """ Use for Production """
    if os.getenv("SECRET_KEY") is not None:
        SECRET_KEY = str(os.getenv("SECRET_KEY"))

    if os.getenv("PORT") is not None:
        PORT = os.getenv("PORT")


class DevelopmentConfig(Config):
    """ Config for Development """
    DEBUG = True

    if os.getenv("SECRET_KEY") is not None:
        SECRET_KEY = str(os.getenv("SECRET_KEY"))

    if os.getenv("PORT") is not None:
        PORT = os.getenv("PORT")
