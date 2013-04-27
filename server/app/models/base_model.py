# -*- coding: utf-8 -*-
from sqlalchemy import Column
from sqlalchemy.types import *
from sqlalchemy.ext.declarative import declarative_base

SqlBaseModel = declarative_base()

#
# class BaseModel(SqlBaseModel):
#
#     __tablename__ = 'default'
#
#     id = Column(Integer, primary_key=True)
#     pass


