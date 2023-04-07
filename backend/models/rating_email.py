from sqlalchemy import Integer, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from config.db import Base
from sqlalchemy.orm import relationship
import datetime

class EmailRatingModel(Base):
    __tablename__ = 'emailRating'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    idea_id = Column(Integer, ForeignKey('ideas.id'), unique=False)
    email = Column(String(255), unique=False)
    rating = Column(String(255))
    feedback = Column(String(1024))
    created_date = Column(DateTime, default= datetime.datetime.utcnow)

    emailRating = relationship('IdeasModel', back_populates="emails")


    # def to_json_for_all_user(self):
    #     return {
    #         "id": str(self.id),
    #         "username": str(self.username)
    #     }