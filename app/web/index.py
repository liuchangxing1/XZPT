# -*- coding: utf-8 -*-
# @Time : 2020/7/17 15:12
# @Author : Feng Bo
# @File : index
# @Description :

from flask import render_template
# from flask_login import login_required

from . import web


@web.route('/')
# @login_required
def index():
    return render_template('index.html')

