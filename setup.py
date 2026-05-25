from app.database.connection import Base,engine
from app.models.user_model import User
from app.models.product_model import Product
from app.models.feedback_model import Feedback
Base.metadata.create_all(bind=engine)

#Running this will create tables
print("Tables created successfully")