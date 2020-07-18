import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # use either local env variable or a set one if that is not available
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'jJ4NE5H2n2R6Ly'

    # db setup
    # I'm pretty sure the backslash escapes the newline so this can multi line without 
    # whitespace issues
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False