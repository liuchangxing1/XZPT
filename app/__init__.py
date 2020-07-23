# -*- coding: utf-8 -*-
# @Time : 2020/7/14 21:44
# @Author : Feng Bo
# @File : __init__.py
# @Description : package app 初始化文件

from flask import Flask
from app.models.base import db
#from flask_login import LoginManager

#login_manager = LoginManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    # db.init_app(app)
    # login_manager.init_app(app)
    # login_manager.login_view = 'web.login'
    # login_manager.login_message = '请登录'
    # with app.app_context():
    #     db.create_all()
    return app


def register_blueprint(app):
    from app.web import web
    app.register_blueprint(web)
