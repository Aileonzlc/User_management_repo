#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

import json
import logging
import os

from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

from UserManagementBackend.UserManagementError import ConfigNotFoundError, ConfigFileError

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
# model元类
Base = declarative_base()


class Users(Base):
    """用户信息表"""
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False, unique=True)
    password = Column(String(40), nullable=False)
    remote_identity = Column(String(10), ForeignKey('Auths.identity'))
    # Users下有个属性auth用于储存它对应的权限, 多个user对应一个auth
    auth = relationship("Auths", back_populates="users")

    def __repr__(self):
        return f"<User(name='{self.name}', password='{self.password}', identity='{self.remote_identity}')>"

    def __str__(self):
        return self.__repr__()


class Auths(Base):
    """权限信息表"""
    __tablename__ = 'Auths'

    identity = Column(String(10), primary_key=True)
    authority = Column(Integer, nullable=False)
    # rg_password = Column(Integer, nullable=False)

    # Auths下有个users属性用于储存它对应的用户，多个user对应一个auth
    users = relationship("Users", order_by=Users.id, back_populates="auth")

    def __repr__(self):
        return f"<Address(email_address='{self.identity}',authority='{self.authority}')>"

    def __str__(self):
        return self.__repr__()


path = os.path.dirname(__file__)
logging.info(f'config.json path is {path}')

try:
    with open(f'{path}/config.json', 'r', encoding='utf-8') as f:
        config_data = json.load(f)
    mysql_user = config_data['user']
    mysql_pwd = config_data['password']
    mysql_host = config_data['host']
    mysql_port = config_data['port']
    mysql_db = config_data['database']
    mysql_encoding = config_data['encoding']
except FileNotFoundError as e:
    logging.info(e)
    raise ConfigNotFoundError('找不到config.json文件')
except KeyError as e:
    logging.info(e)
    raise ConfigFileError('配置文件格式有误！')

try:
    # 通过create_engine()可以连接数据库
    engine = create_engine(f'mysql+pymysql://{mysql_user}:{mysql_pwd}@{mysql_host}:{mysql_port}/{mysql_db}',
                           encoding=mysql_encoding,
                           # echo=True
                           )
    # 使用Base类的metadata来创建表
    Base.metadata.create_all(engine)
except RuntimeError as r:
    logging.error(f'RuntimeError-{r}')
    raise RuntimeError
# 创建一个监听mysql服务的工厂类
Session = sessionmaker(bind=engine)


if __name__ == "__main__":
    # 测试代码
    session = Session()
    query = session.query(Users).filter(Users.name == 'zz')
    try:
        user = query.one()
        if user:
            logging.info(f'{user}')
            logging.info(f'{user.auth}')
    finally:
        session.close()

