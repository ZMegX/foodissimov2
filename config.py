import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'fallback-secret')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    DEBUG = True

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://testserver_pbjv_user:4y1kfym9fAj9I4GE9GTFgmY1VP0TEnes@dpg-d0rna6ili9vc73av1akg-a/testserver_pbjv')    
    DEBUG = False

config_by_name = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
