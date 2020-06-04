#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from abc import ABCMeta, abstractmethod
from UserManagementBackend.UserORM import Session, Users, Auths
import logging


class QueryInterface(metaclass=ABCMeta):
    @abstractmethod
    def query(self, *, identity: str = None, str_in_name: str = None) -> list:
        pass


class Query(QueryInterface):
    def query(self, *, identity: str = None, str_in_name: str = None) -> list:
        logging.info(f'query through identity={identity}, name field contains {str_in_name} string')
        session = Session()
        q = session.query(Users.name, Users.password, Users.remote_identity, Auths.authority). \
            join(Auths)  # filter(Users.remote_identity == Auths.identity)

        if identity:
            q = q.filter(Users.remote_identity == identity)
        if str_in_name:
            q = q.filter(Users.name.like('%' + str_in_name + '%'))
        q.order_by(Users.remote_identity)
        try:
            users = q.all()
            users_list = [
                {
                    'name': user[0],
                    'password': user[1],
                    'remote_identity': user[2],
                    'authority': user[3],
                } for user in users
            ]
        finally:
            session.close()
        logging.info(f'{len(users_list)} users were found')
        return users_list


if __name__ == "__main__":
    urs = Query().query(identity='管理员', str_in_name='z')
    print(urs)
