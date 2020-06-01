#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

"""
Required:
pip install cryptography; # 加密解密，连接mysql需要使用，否则可能报错
pip install pymysql; # 连接mysql的api
pip install sqlalchemy; # 连接mysql的orm
"""
"""
本包下所有模块默认数据库连接正常，库表设计正常，故不对数据库连接及库表设计不正确产生的错误进行处理
"""
"""
本包使用方法：
1、注册功能
Register().register(用户名, 用户密码, 用户身份, 注册口令)  # 写入数据库，无返回值
2、登陆功能
login_user = LoginUser(LoginFactoryEncrypt().create_user(用户名, 用户密码))  # 读取数据库，返回一个包含该用户所有信息的LoginUser对象
"""