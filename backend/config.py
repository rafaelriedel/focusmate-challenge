"""Configuration File."""
import os


class Config(object):
    """Parent configuration class."""

    DEBUG = True
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    DOMAIN_NAME = 'http://localhost'


class DevelopmentDockerConfig(Config):
    """Configuration for docker development."""

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1q2w3e4r5t@focusmate-db/focusmate'
    DEBUG = True


class DevelopmentConfig(Config):
    """Configuration for development."""

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1q2w3e4r5t@localhost/focusmate'
    DEBUG = True


app_config = {
    'development': DevelopmentConfig,
    'developmentDocker': DevelopmentDockerConfig,
}
