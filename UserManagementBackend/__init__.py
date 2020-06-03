#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

"""
依赖包:
pip install cryptography; # 加密解密，连接mysql需要使用，否则可能报错
pip install pymysql; # 连接mysql的api
pip install sqlalchemy; # 连接mysql的orm
"""
"""
准备工作：
1、在MySQL中新建一个数据库，数据库名自定义，例如为test
2、在test数据库中运行当前文件夹下的LoginTables.sql执行用户登陆信息表的导入
3、修改config.json, 把MySQL的登陆用户（这个用户必须有读写test数据库的权限）名填到user行，如 user："root"
类似修改密码password，端口port，和数据库名database
"""
"""
本包下所有模块默认数据库连接正常，库表设计正常，故不对数据库连接及库表设计不正确产生的错误进行处理
由于配置不正确产生的错误有：
ConfigNotFoundError  # 文件路径有误
ConfigFileError  # 配置文件格式有误
RuntimeError  # 连接数据库失败
"""
"""
本包使用方法：
1、注册功能

Register().register(用户名, 用户密码, 用户身份)  # 将用户名，用户密码，用户身份写入数据库，无返回值
可能产生的错误：
InputIsNoneError  # 输入有误
IdentityDoesNotExistError  # 注册身份不存在
UserExistError # 用户名已存在，不可进行注册

2、登陆功能
login_user = LoginUser(LoginFactoryEncrypt().create_user(用户名, 用户密码))  # 读取数据库，返回一个包含该用户所有信息的LoginUser对象
可能产生的错误：
PasswordError  # 密码错误
UserDoesNotExistError  # 用户不存在
"""