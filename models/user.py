from sqlalchemy import Column, String, Boolean
from database.database import Base


class User(Base):
    __tablename__ = 'users'
    email = Column(String(120), primary_key=True)
    password = Column(String(200))
    first_name = Column(String(50))
    last_name = Column(String(50))
    isStudent = Column(Boolean())

    def __init__(self, email=None, password=None, first_name=None, last_name=None, isStudent=None):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.isStudent = isStudent

    def __repr__(self):
        return f"{self.email}"



