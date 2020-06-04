#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from abc import ABCMeta, abstractmethod
from UserManagementBackend.UserORM import Users, Session
from UserManagementBackend.PasswordEncrypt import sha1_encrypt
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
import logging
from UserManagementBackend.UserManagementError import UserDoesNotExistError, IdentityDoesNotExistError, UserExistError


class UpdateInterface(metaclass=ABCMeta):
    """抽象产品，更新"""
    @abstractmethod
    def update_name(self, user: Users, new_name: str):
        pass

    @abstractmethod
    def update_password(self, user: Users, new_password: str):
        pass

    @abstractmethod
    def update_identity(self, user: Users, new_identity: str):
        pass

    @abstractmethod
    def update(self, old_name: str, *, new_name: str = None, new_password: str = None, new_identity: str = None):
        pass


class Update(UpdateInterface):
    """具体产品，更新"""
    def update_name(self, user: Users, new_name: str):
        if not new_name:  # 不能为None，也不能为none
            return
        user.name = new_name

    def update_password(self, user: Users, new_password: str):
        if not new_password:  # 不能为None，也不能为none
            return
        hex_password = sha1_encrypt(new_password)
        user.password = hex_password

    def update_identity(self, user: Users, new_identity: str):
        if not new_identity:  # 不能为None，也不能为none
            return
        user.remote_identity = new_identity

    def update(self, old_name: str, *, new_name: str = None, new_password: str = None, new_identity: str = None):
        logging.info(f'prepare to update user {old_name}, new information {new_name, new_password, new_identity}')
        if all(map(lambda x: x is None, [new_name, new_password, new_identity])):
            return
        session = Session()
        query = session.query(Users).filter(Users.name == old_name)
        try:
            user = query.one()  # NoResultFound
            self.update_name(user, new_name)
            self.update_password(user, new_password)
            self.update_identity(user, new_identity)
            session.commit()
            logging.info(f'old user {old_name} has been updated')
        except NoResultFound:
            logging.info(f'user {old_name} does not exist')
            raise UserDoesNotExistError(f'用户 {old_name} 不存在')
        except IntegrityError as e:
            logging.info(f'database IntegrityError, error code {e.orig.args[0]}')
            session.rollback()
            if e.orig.args[0] == 1452:
                raise IdentityDoesNotExistError(f'新用户身份 {new_identity} 不存在')
            else:
                assert e.orig.args[0] == 1062
                raise UserExistError(f'新用户名 {new_name} 已存在，无法进行更新')
        finally:
            session.close()


if __name__ == '__main__':
    Update().update(old_name='xxx', new_name='root', new_password='123')
