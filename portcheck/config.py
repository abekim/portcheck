#
# @author Cory Dolphin
# @wcdolphin
#
import os


class Config(object):
    """
    Basic default global configuration variables not specific to any environment
    """
    SECRET_KEY = os.urandom(24)
    DEBUG = True


class DevelopmentConfig(Config):
    """ 
    The Development Configuration, provides default database and facebook credentials and
    configuration to run the application
    """
    CACHE_TYPE = 'null'
    CACHE_DEFAULT_TIMEOUT = 24*60*60
    CACHE_THRESHOLD = 1000


def configure(app):

    try:
        app.config.from_object('main.production_config')
        print app.config
    except ImportError as e:
        app.config.from_object(DevelopmentConfig)
        print "WARNING: Initialized in Development mode"
