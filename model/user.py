from sqlalchemy import Column, String

from model.base import BaseTable


class User(BaseTable):
    __tablename__ = "user"

    email = Column(String, unique=True, index=True)
    password = Column(String)
