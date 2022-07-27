# coding: utf-8
import sqlalchemy.ext.declarative

BaseModel = sqlalchemy.ext.declarative.declarative_base()


class UserModel(BaseModel):
    __table__ = "user"


class RoleModel(BaseModel):
    __table__ = "role"


def InitializeModel(engine):
    pass
