# -*- coding: utf-8 -*-
from models.base_model import *


class User(DataBaseModel):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(30), unique=True, index=True)
    password = Column(VARCHAR(20))
    email = Column(VARCHAR(30))
    nickname = Column(VARCHAR(20))
    role = Column(INTEGER(3))
    activated = Column(INTEGER(3))
    create_time = Column(VARCHAR(20))
    last_login_time = Column(VARCHAR(20))

    def saveNew(self):
        db_session.add(self)
        db_session.commit()
