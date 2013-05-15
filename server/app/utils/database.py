# -*- coding: utf-8 -*-
from config import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

mysql_engine = create_engine(database.DB_ADDRESS, **database.DB_CONFIG)

DB_Session = sessionmaker(bind=mysql_engine)

DataBaseModel = declarative_base()

def getSession():
    return DB_Session()

def create_db():
    from models import *
    # DataBaseModel.metadata.drop_all(mysql_engine)
    DataBaseModel.metadata.create_all(mysql_engine)



