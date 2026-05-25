from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.product_routes import router as product_router
from app.routes.feedback_routes import router as feedback_router
from app.routes.product_feedback_routes import router as product_feedback_router

app = FastAPI(title="NeonDB + FastAPI demo")

app.include_router(user_router)
app.include_router(product_router)
app.include_router(feedback_router)
app.include_router(product_feedback_router)

########## HOME ROUTE #############
@app.get("/")
def home():
    return {"message" : "FastAPI and Neon DB running"}




