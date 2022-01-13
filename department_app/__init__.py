from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = '4b64752afacf6d42c79e31c7dc32e27a01b273b1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from department_app.views import views

from department_app.rest import api
app.register_blueprint(api, url_prefix='/api')
