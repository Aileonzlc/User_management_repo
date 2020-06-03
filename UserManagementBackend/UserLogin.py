#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from abc import ABCMeta, abstractmethod
from UserManagementBackend.UserORM import Users, Auths, Session
from sqlalchemy.orm.exc import NoResultFound
import logging
from UserManagementBackend.UserManagementError import PasswordError, UserDoesNotExistError, UserExistError
from UserManagementBackend.PasswordEncrypt import sha1_encrypt


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def password_verify(self, password: str, db_password: str) -> bool:
        pass

    def create_user(self, name: str, password: str) -> Users:
        logging.info(f'input information -> login name: {name}, login password: {password}')
        # 会话工厂生产一个具体会话
        session = Session()
        query = session.query(Users).filter(Users.name == name)
        try:
            # 可能产生NoResultFound错误
            u = query.one()
            # 提交事务
            session.commit()
            # 把值都存到新对象里
            auth = Auths(identity=u.auth.identity, authority=u.auth.authority, rg_password=u.auth.rg_password)
            user = Users(id=u.id, name=u.name, password=u.password, remote_identity=u.remote_identity, auth=auth)
        except NoResultFound:
            raise UserDoesNotExistError('用户不存在！')
        finally:
            # 关闭会话
            session.close()

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
    def modify_name(self, new_name: str):
        pass

    @abstractmethod
    def modify_password(self, new_password: str):
        pass


class LoginUser(Singleton):
    def __init__(self, user: Users):
        """
        :type user: Users
        """
        self._authority = user.auth.authority
        self.user = user
        logging.info(f'login information -> login user: {user.name}, '
                     f'memory address: {id(self)}, authority: {self._authority}')

    def get_authority(self):
        return self._authority

    def modify_name(self, new_name: str):
        logging.info(f'prepare update user name from {self.user.name} to {new_name}')
        session = Session()
        query_new_name = session.query(Users).filter(Users.name == new_name)

        # 如果用户名已经存在，引起错误
        if query_new_name.one_or_none():
            raise UserExistError(f'用户名 {new_name} 已存在')

        # 用户名不存在，则更新用户名
        query = session.query(Users).filter(Users.id == self.user.id)
        try:
            u = query.one()
            u.name = new_name
            session.commit()
            # 事务提交后要更新下当前的用户名
            self.user.name = new_name
        except NoResultFound:
            raise UserDoesNotExistError(f'用户不存在, 当前用户 {self.user} 已失效！')
        finally:
            session.close()
        logging.info(f'user name been changed to {new_name}')

    def modify_password(self, new_password: str):
        logging.info(f'prepare update user password to {new_password}')
        session = Session()
        query = session.query(Users).filter(Users.id == self.user.id)
        try:
            u = query.one()
            hex_password = sha1_encrypt(new_password)
            u.password = hex_password
            session.commit()
            # 事务提交后要更新下当前的用户密码
            self.user.password = hex_password
        except NoResultFound:
            raise UserDoesNotExistError(f'用户不存在, 当前用户 {self.user} 已失效！')
        finally:
            session.close()
        logging.info(f'user password been changed to {new_password}')


if __name__ == '__main__':
    # 测试代码
    _user = LoginFactoryEncrypt().create_user('zz', '123')
    login_user = LoginUser(_user)
    login_user.modify_name('aa')
    login_user.modify_password('333')
