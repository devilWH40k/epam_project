from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from department_app.config import Config

db = SQLAlchemy()


def create_app(test_config=None):
    app = Flask(__name__, template_folder='templates', static_folder='static')

    if test_config:
        app.config.from_object(test_config)
    else:
        app.config.from_object(Config)

    db.init_app(app)

    from department_app.rest import api as api_blueprint
    from department_app.views import main as main_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(main_blueprint)

    return app
