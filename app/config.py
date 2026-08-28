import os


class Config:
    """Base application configuration."""

    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "dev-secret-key-change-in-production"
    )
    TESTING = False


class TestingConfig(Config):
    """Configuration used when running tests."""

    TESTING = True


class DevelopmentConfig(Config):
    """Configuration used during development."""

    DEBUG = True


class ProductionConfig(Config):
    """Configuration used in production."""

    DEBUG = False
