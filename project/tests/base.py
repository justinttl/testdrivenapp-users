"""Define base test case."""

from flask_testing import TestCase

from project import app, db


class BaseTestCase(TestCase):
    """Base test case."""

    def create_app(self):
        """Initialize flask app from testing config."""
        app.config.from_object("project.config.TestingConfig")
        return app

    def setUp(self):
        """Set up db tables before test method."""
        db.create_all()
        db.session.commit()

    def tearDown(self):
        """Drop db tables and remove db sessions."""
        db.session.remove()
        db.drop_all()
