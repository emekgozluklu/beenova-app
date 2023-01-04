from flask import Flask
from beenova_app import views


def create_app():
    app = Flask(__name__)

    # add url rules
    app.add_url_rule("/", view_func=views.index)

    return app
