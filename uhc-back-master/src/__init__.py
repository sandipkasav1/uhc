from flask import Flask

from . import api, pages

def create_app():
    app = Flask(__name__)

    app.register_blueprint(pages.bp)
    app.register_blueprint(api.bp, url_prefix="/api")

    return app