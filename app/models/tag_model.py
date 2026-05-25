from app.database.connection import Base
from sqlalchemy import Column,String,Integer

class Tag(Base):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)