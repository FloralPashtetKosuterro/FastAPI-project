from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .database import Base


class Clients(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String, unique=False, index=False)
    name = Column(String, unique=False, index=False)
