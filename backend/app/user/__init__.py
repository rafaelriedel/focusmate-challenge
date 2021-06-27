"""User blueprints.

This file is reponsible for mapping user's view blueprint

"""
from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

from . import views