"""__init__ file of views package with imported blueprint and views module."""

from flask import Blueprint

main = Blueprint('main', __name__)

from department_app.views import views
