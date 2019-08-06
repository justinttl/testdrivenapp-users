"""Define User APIs."""

from flask import Blueprint
from flask_restful import Api, Resource

users_blueprint = Blueprint("users", __name__)
api = Api(users_blueprint)


# User View
class UserPing(Resource):
    """User Ping model."""

    def get(self):
        """Get a pong back."""
        return {"status": "success", "message": "pong!"}


# Routes
api.add_resource(UserPing, "/users/ping")
