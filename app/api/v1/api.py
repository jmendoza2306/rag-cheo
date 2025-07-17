# app/api/v1/api.py
from fastapi import APIRouter
from app.api.v1.webhooks import notion

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(
    notion.router, 
    prefix="/notion", 
    tags=["Notion"]
)



# Aquí puedes agregar más routers cuando los tengas
# api_router.include_router(users.router, prefix="/users", tags=["Users"])
# api_router.include_router(products.router, prefix="/products", tags=["Products"])