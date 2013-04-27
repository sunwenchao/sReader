# -*- coding: utf-8 -*-
from models.base_model import *


class User(SqlBaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(20))
    password = Column(VARCHAR(20))
    nickname = Column(VARCHAR(20))
    role = Column(INTEGER(3))
    activated = Column(INTEGER(3))
    create_time = Column(VARCHAR(20))
    last_login_time = Column(VARCHAR(20))

    def ccc(self):
        print 'ccccc'

ss = {
    'username': 'sunstyle',
    'password': '123123',
    'nickname': '李白',
    'role': 1,
    'activated': 1,
    'create_time': '1231231231232',
    'last_login_time': '1231231231232'
}

a = User(**ss)

from utils import database

SqlBaseModel.metadata.drop_all(database.mysql_engine)
SqlBaseModel.metadata.create_all(database.mysql_engine)

session = database.getSession()

session.add(a)
session.commit()

qqq = session.query(User).get(1)

qqq.ccc()