from server import app
import pytest


class Test:
    def test_homepage(self):
        with app.test_request_context('/'):
            assert ("Home page")
