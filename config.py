import os

class Config(object):
    # use either local env variable or a set one if that is not available
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jJ4NE5H2n2R6Ly'