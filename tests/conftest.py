import pytest
# from app.app import app as flask_app

# @pytest.fixture
# def app():
#     flask_app.config.update({
#         "TESTING": True
#     })
#     yield flask_app

# create a flask app to test
# can then do fake tests using API in which allows the pytest

from flask import Flask

@pytest.fixture
def app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {"message": "Travel Blog API running"}

    @app.route("/posts")
    def posts():
        return []

    app.config["TESTING"] = True
    return app

# attempt new way as kept failing due to Greenlet