"""Application configurations."""

import os


class Config:
    """Default config."""

    SECRET_KEY = os.environ.get('SECRET_KEY') or '4b64752afacf6d42c79e31c7dc32e27a01b273b1'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
