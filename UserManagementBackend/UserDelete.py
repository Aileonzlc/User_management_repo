#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from UserManagementBackend.UserManagementError import UnknownInputTypeError, UserDoesNotExistError
from UserManagementBackend.UserORM import Users, Session
from sqlalchemy.orm.exc import NoResultFound
import logging
import copy


class Delete:
    @staticmethod
    def delete_set(name_set: set):
        # 避免对容器类型数据直接操作
        internal_name_set = copy.copy(name_set)
        logging.info(f'these users {internal_name_set} prepare to be deleted')
        session = Session()
        query = session.query(Users).filter(Users.name.in_(internal_name_set))
        try:
            users = query.all()
            for user in users:
                internal_name_set.remove(user.name)
                session.delete(user)
            if len(internal_name_set) != 0:
                session.rollback()
                logging.info(f'thest users {internal_name_set} do not exist, transaction has been rollbacked')
                raise UserDoesNotExistError(f'这些用户不存在 {internal_name_set}')
            session.commit()
            logging.info(f'all users have been deleted')
        finally:
            # 关闭会话
            session.close()

    @staticmethod
    def delete_single(name: str):
        logging.info(f'user {name} prepare to be deleted')
        session = Session()
        query = session.query(Users).filter(Users.name == name)
        try:
            user = query.one()
            session.delete(user)
            session.commit()
            logging.info(f'user {name} has been deleted')
        except NoResultFound:
            session.rollback()
            logging.info(f'fail to delete user {name}')
            raise UserDoesNotExistError(f'用户 {name} 不存在')
        finally:
            session.close()

    def delete(self, name):
        if type(name) == set:
            self.delete_set(name)
        elif type(name) == str:
            self.delete_single(name)
        else:
            raise UnknownInputTypeError(f'unknown input type {name}')


if __name__ == "__main__":
    Delete().delete({'zz', 'z'})
