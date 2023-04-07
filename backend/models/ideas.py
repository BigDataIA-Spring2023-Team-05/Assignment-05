from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import Base
from sqlalchemy.orm import relationship
import datetime

class IdeasModel(Base):
    __tablename__ = 'ideas'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'), unique=False)
    idea_title = Column(String(255))
    features = Column(String(1024))
    created_date = Column(DateTime, default= datetime.datetime.utcnow)

    idea = relationship('UserModel', back_populates="user")
    emails = relationship("EmailRatingModel", back_populates="emailRating")

