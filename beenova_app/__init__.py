from flask import Flask
from beenova_app import views, auth


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'too_secret'

    # add url rules
    app.add_url_rule("/", view_func=views.index)
    app.register_blueprint(auth.bp)

    return app
