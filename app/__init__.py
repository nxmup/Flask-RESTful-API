from flask import Flask


def create_app():
    app = Flask(__name__)

    from .api_1_0 import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1.0')

    return app