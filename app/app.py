#coding:utf8
#
from flask import Flask
from app.views import init_views
from app.ext import init_ext

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('mysettings.py')
    init_views(app)
    init_ext(app)
    return app

