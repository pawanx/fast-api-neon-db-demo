from app.database.connection import Base
from sqlalchemy import Column,Integer,String,Boolean

class Product(Base) :
    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    quantity = Column(Integer, default=0)
    in_stock = Column(Boolean, default=True)
    is_archieved = Column(Boolean,default=False)