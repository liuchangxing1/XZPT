# -*- coding: utf-8 -*-
# @Time : 2020/7/14 21:43
# @Author : Feng Bo
# @File : xzpt.py
# @Description : flask 入口文件

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
