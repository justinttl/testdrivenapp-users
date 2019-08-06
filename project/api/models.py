"""Define user model."""

from sqlalchemy.sql import func

from project import db


class User(db.Model):  # type: ignore
    """User Model."""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, username, email):
        """Initialize a user object."""
        self.username = username
        self.email = email
