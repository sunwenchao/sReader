# -*- coding: utf-8 -*-
from config import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

mysql_engine = create_engine(database.DB_ADDRESS, **database.DB_CONFIG)

DB_Session = sessionmaker(bind=mysql_engine)


def getSession():
    return DB_Session()

