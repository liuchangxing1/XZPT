# -*- coding: utf-8 -*-
# @Time : 2020/7/23 15:54
# @Author : Feng Bo
# @File : func1
# @Description :

from flask import render_template
from flask_login import login_required
from . import web

@web.route('/func1', methods=['GET', 'POST'])
# @login_required
def func1():
    return render_template('func1.html')