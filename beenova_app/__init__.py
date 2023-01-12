from flask import Flask
from beenova_app import views, auth, admin, application
import os


def create_app(test_config=None):
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'beenova.sqlite'),
        UPLOAD_FOLDER=os.path.join(app.instance_path, 'uploads'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.add_url_rule("/", view_func=views.index)
    app.register_blueprint(auth.bp)
    app.register_blueprint(admin.bp)
    app.register_blueprint(application.bp)

    from . import db
    db.init_app(app)

    return app
