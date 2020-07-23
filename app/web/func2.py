# -*- coding: utf-8 -*-
# @Time : 2020/7/23 16:52
# @Author : Feng Bo
# @File : func2
# @Description :

from flask import render_template
from . import web

@web.route('/func2', methods=['GET', 'POST'])
# @login_required
def func2():
    return render_template('func2.html')