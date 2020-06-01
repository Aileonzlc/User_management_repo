#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'


class PasswordError(Exception):
    """自定义异常，用户密码输入错误"""
    def __init__(self, info='用户密码错误！'):
        # 调用Exception的init方法去完成自己的一个初始化
        Exception.__init__(self)
        # 新添加了一个变量，用于自定义错误信息
        self.error_info = info

    def __str__(self):
        # 这个方法是为了支撑print语句，打印出用户自己定义的错误信息
        return f"PasswordError:{self.error_info}"


class UserDoesNotExistError(Exception):
    """自定义异常，用户不存在"""
    def __init__(self, info='用户不存在！'):
        # 调用Exception的init方法去完成自己的一个初始化
        Exception.__init__(self)
        # 新添加了一个变量，用于自定义错误信息
        self.error_info = info

    def __str__(self):
        # 这个方法是为了支撑print语句，打印出用户自己定义的错误信息
        return f"UserDoesNotExistError:{self.error_info}"


class IdentityDoesNotExistError(Exception):
    """自定义异常，不存在该身份"""
    def __init__(self, info='不存在该身份！'):
        # 调用Exception的init方法去完成自己的一个初始化
        Exception.__init__(self)
        # 新添加了一个变量，用于自定义错误信息
        self.error_info = info

    def __str__(self):
        # 这个方法是为了支撑print语句，打印出用户自己定义的错误信息
        return f"IdentityDoesNotExistError:{self.error_info}"


class RegisterPasswordError(Exception):
    """自定义异常，注册口令输入错误"""
    def __init__(self, info='注册口令输入错误！'):
        # 调用Exception的init方法去完成自己的一个初始化
        Exception.__init__(self)
        # 新添加了一个变量，用于自定义错误信息
        self.error_info = info

    def __str__(self):
        # 这个方法是为了支撑print语句，打印出用户自己定义的错误信息
        return f"RegisterPasswordError:{self.error_info}"


class UserExistError(Exception):
    """自定义异常，用户名已存在"""
    def __init__(self, info='用户名已存在！'):
        # 调用Exception的init方法去完成自己的一个初始化
        Exception.__init__(self)
        # 新添加了一个变量，用于自定义错误信息
        self.error_info = info

    def __str__(self):
        # 这个方法是为了支撑print语句，打印出用户自己定义的错误信息
        return f"UserExistError:{self.error_info}"
