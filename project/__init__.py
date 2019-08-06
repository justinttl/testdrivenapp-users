"""Define User microservice."""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from project.api.users import users_blueprint

db = SQLAlchemy()


def create_app(script_info=None):
    """Create a flask app through factory pattern."""
    # App
    app = Flask(__name__)

    # Set configuration
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)

    # Extensions
    db.init_app(app)

    # Blueprints
    app.register_blueprint(users_blueprint)

    # Shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app
