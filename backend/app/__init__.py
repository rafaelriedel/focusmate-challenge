"""Application creation file."""

import os

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from flask_cors import CORS

from config import app_config

db = SQLAlchemy()


def create_app(config_name):
    """Create new flask application.

    Parameters:
        config_name : str
            desired configuration name

    Returns:
        a flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    CORS(app)

    app.config.from_object(app_config[os.getenv('APP_SETTINGS')])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    Migrate(app, db)

    from .session import session_blueprint

    app.register_blueprint(session_blueprint)

    from .user import user_blueprint

    app.register_blueprint(user_blueprint)

    return app
