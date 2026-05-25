from app.database.connection import Base
from sqlalchemy import Column,Integer,String


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer,primary_key=True,index=True)
    #nullable = False means required
    name = Column(String, nullable=False)
    comment = Column(String, nullable=False)