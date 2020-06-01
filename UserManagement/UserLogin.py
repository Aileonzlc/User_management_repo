#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from abc import ABCMeta, abstractmethod
from UserManagement.UserORM import Users, Session
from sqlalchemy.orm.exc import NoResultFound
import logging
from UserManagement.UserManagementError import PasswordError, UserDoesNotExistError
from UserManagement.PasswordEncrypt import sha1_encrypt


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def password_verify(self, password: str, db_password: str) -> bool:
        pass

    def create_user(self, name, password):
        logging.info(f'input information -> login name: {name}, login password: {password}')
        # 会话工厂生产一个具体会话, 保持这个会话不关闭，以后这个登陆用户的操作都要基于这个会话
        session = Session()
        query = session.query(Users).filter(Users.name == name)
        try:
            # 可能产生NoResultFound错误
            user = query.one()
            # 提交事务
            session.commit()
        except NoResultFound:
            raise UserDoesNotExistError('用户不存在！')

        # 获得user则用户存在，进一步校验密码
        if password is None:
            raise PasswordError('密码不能为空！')
        if not self.password_verify(password, user.password):
            raise PasswordError('密码不正确！')
        # 密码校验通过，返回一个user对象
        logging.info(f'login user -> {user.name}: {user}')
        return user


class LoginFactorySimple(Factory):
    """使用明文密钥的具体工厂"""
    def password_verify(self, password, db_password):
        if password == db_password:
            return True
        else:
            return False


class LoginFactoryEncrypt(Factory):
    """使用sha1加密的具体工厂"""
    def password_verify(self, password: str, db_password: str) -> bool:
        logging.info(f'input password -> {password}')
        hex_password = sha1_encrypt(password)  # sha1加密
        logging.info(f'password to db_password -> {hex_password}')
        if db_password == hex_password:  # 判断数据库中保存的密码是否与用户输入密码相同
            return True
        else:
            return False


class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    @abstractmethod
    def get_authority(self):
        pass

    @abstractmethod
    def modify_name(self):
        pass

    @abstractmethod
    def modify_password(self):
        pass


class LoginUser(Singleton):
    def __init__(self, user: Users):
        """
        :type user: Users
        """
        self._authority = user.auth.authority
        logging.info(f'login information -> login user: {user.name}, '
                     f'memory address: {id(self)}, authority: {self._authority}')

    def get_authority(self):
        return self._authority

    def modify_name(self):
        pass

    def modify_password(self):
        pass


if __name__ == '__main__':
    # 测试代码
    u = LoginFactoryEncrypt().create_user('xx', '123x')
    login_user = LoginUser(u)
