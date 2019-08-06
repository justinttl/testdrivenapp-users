"""Define User microservice."""

import os

from flask import Flask, jsonify
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

# Setup app
app = Flask(__name__)
api = Api(app)


# Set config and db connections
app.config.from_object("project.config.DevelopmentConfig")
app_settings = os.getenv("APP_SETTINGS")
app.config.from_object(app_settings)
db = SQLAlchemy(app)


# Model Definition
class User(db.Model):  # type: ignore
    """User Model."""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        """Initialize a user object."""
        self.username = username
        self.email = email


# User View
class UserPing(Resource):
    """User Ping model."""

    def get(self):
        """Get a pong back."""
        return {"status": "success", "message": "pong!"}


# Routes
api.add_resource(UserPing, "/users/ping")
