#!/usr/bin/python3
"""
creat a flask app blueprint
"""
from flask import blueprints

app_views = Blueprints('app_views', __name__, url_prefix'/api/v1')

from api.v1.views.index import *