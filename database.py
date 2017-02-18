"""
Document stuff
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# TODO: Create classes
class Notification(Base):
    """

    """
    __tablename__ = 'notification'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
