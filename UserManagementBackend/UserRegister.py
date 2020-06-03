#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from abc import ABCMeta, abstractmethod
from UserManagementBackend.UserORM import Users, Auths, Session
from UserManagementBackend.UserManagementError import RegisterPasswordError, UserExistError, IdentityDoesNotExistError
from sqlalchemy.orm.exc import NoResultFound
from UserManagementBackend.PasswordEncrypt import sha1_encrypt
import logging


class RegisterFactory(metaclass=ABCMeta):
    """注册器抽象类"""
    @abstractmethod
    def register_password_verify(self, identity: str, register_password: int) -> bool:
        # 验证注册口令的过程
        pass

    @abstractmethod
    def identity_verify(self, name: str) -> bool:
        # 验证名称是否已存在过程
        pass

    @abstractmethod
    def register_user(self, name: str, password: str, identity: str, register_password: int) -> bool:
        # 调用orm的User的add函数添加新纪录
        pass

    def register(self, name: str, password: str, identity: str, register_password: int):
        logging.info(f"""register information -> name: {name}, password: {password}, identity: {identity}, 
                     register_password: {register_password}""")
        if not self.register_password_verify(identity, register_password):
            raise RegisterPasswordError('注册口令输入错误！')
        if not self.identity_verify(name):
            raise UserExistError('用户名已存在！')
        if self.register_user(name, password, identity, register_password):
            logging.info(f'user has been register -> name: {name}, password: {password}, identity: {identity}')
        else:
            logging.info(f'fail to register user -> name: {name}, password: {password}, identity: {identity} '
                         f'because')


class Register(RegisterFactory):
    """具体注册器"""
    def register_password_verify(self, identity: str, register_password: int) -> bool:
        logging.info(f'input rg_password -> {register_password}')
        # 会话工厂生产一个具体会话
        session = Session()
        query = session.query(Auths.rg_password).filter(Auths.identity == identity)
        try:
            # 可能产生NoResultFound错误
            rg_password = query.one()[0]
            logging.info(f'rg_password in database -> {rg_password}')
        except NoResultFound:
            raise IdentityDoesNotExistError('该身份不存在！')
        finally:
            # 关闭会话
            session.close()

        if rg_password == register_password:
            return True
        else:
            return False

    def identity_verify(self, name: str) -> bool:
        # 会话工厂生产一个具体会话
        session = Session()
        query = session.query(Users).filter(Users.name == name)
        result = False
        try:
            # 产生NoResultFound错误则表示用户名没有被注册过
            query.one()
            # 否则用户名已存在
        except NoResultFound:
            # 用户名不存在返回真
            result = True
        finally:
            # 关闭会话
            session.close()
        return result

    def register_user(self, name: str, password: str, identity: str, register_password: int) -> bool:
        # 会话工厂生产一个具体会话
        session = Session()
        sha1_password = sha1_encrypt(password)
        new_user = Users(name=name, password=sha1_password, remote_identity=identity)
        result = False
        try:
            # 添加记录
            session.add(new_user)
            # 提交事务
            session.commit()
            result = True
        except Exception as e:
            session.rollback()
            logging.info(f'failure -> {e}')
        finally:
            # 关闭会话
            session.close()

        return result


if __name__ == "__main__":
    # 测试代码
    new = Register().register('aa', '123', '管理员', 1)
