from app.database.connection import Base
from sqlalchemy import Column,Integer,String,Boolean,ForeignKey

class ProductFeedback(Base):
    __tablename__ = "product_feedback"

    id = Column(Integer,primary_key=True,index=True)
    product_id = Column(Integer, ForeignKey("product.id"))
    comment = Column(String)
    rating = Column(Integer)