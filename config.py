import os/
# from distutils.command.config import config
class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://tracy:wangari@localhost/blog'
    SQLALCHEMY_TRACK_MODIFICATIONS= False
class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings.
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings.
    '''
    DEBUG = True
config_options = {
'development':DevConfig,
'production':ProdConfig
}