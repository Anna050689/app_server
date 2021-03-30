class Configuration(object):
    """This class sets configuration settings."""
    DEBUG = True
    SECRET_KEY = 'Secret Key'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:root@localhost:5432/chatbot'
    SQLALCHEMY_TRACK_MODIFICATIONS = False