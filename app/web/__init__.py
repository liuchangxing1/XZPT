# -*- coding: utf-8 -*-
# @Time : 2020/7/17 15:11
# @Author : Feng Bo
# @File : __init__.py
# @Description :

from flask import Blueprint

web = Blueprint('web', __name__)


from app.web import index
from app.web import func1
from app.web import func2