"""__init__ module of rest package with api blueprint and imported routes."""

from flask import Blueprint

api = Blueprint('api', __name__)

from department_app.rest import department_api
from department_app.rest import employee_api
