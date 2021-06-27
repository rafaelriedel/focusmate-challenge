"""Session blueprints.

This file is reponsible for mapping user's view blueprint

"""
from flask import Blueprint

session_blueprint = Blueprint('session', __name__)

from . import views
