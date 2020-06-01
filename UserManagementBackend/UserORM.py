#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Aileon'

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import logging
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
    rg_password = Column(Integer, nullable=False)
    # Auths下有个users属性用于储存它对应的用户，多个user对应一个auth
    users = relationship("Users", order_by=Users.id, back_populates="auth")

    def __repr__(self):
        return f"<Address(email_address='{self.identity}',authority='{self.authority}'" \
               f",register password='{self.rg_password}')>"

    def __str__(self):
        return self.__repr__()


try:
    # 通过create_engine()可以连接数据库
    engine = create_engine('mysql+pymysql://root:767872313@127.0.0.1:3306/test', encoding='utf8', echo=True)
    # 使用Base类的metadata来创建表
    Base.metadata.create_all(engine)
except RuntimeError as r:
    logging.error(f'RuntimeError-{r}')
    raise RuntimeError
# 创建一个监听mysql服务的工厂类
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    # 测试代码
    query = session.query(Users).filter(Users.name == 'zz')
    user = query.one()
    if user:
        logging.info(f'{user}')
        logging.info(f'{user.auth}')

