"""Define User APIs."""

from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# Set config
app.config.from_object('project.config.DevelopmentConfig')


class UserPing(Resource):
    """User Ping model."""

    def get(self):
        """Get a pong back."""
        return {"status": "success", "message": "pong!"}


api.add_resource(UserPing, "/users/ping")
