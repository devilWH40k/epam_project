from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')
    app.config['SECRET_KEY'] = '4b64752afacf6d42c79e31c7dc32e27a01b273b1'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

    db.init_app(app)

    from department_app.rest import api as api_blueprint
    from department_app.views import main as main_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')
    app.register_blueprint(main_blueprint)

    return app