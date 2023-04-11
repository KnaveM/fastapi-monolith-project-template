# app/api/routes/example_route.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def index():
    return {"message": "Hello, this is the index route!"}

@router.get("/example")
async def example_route():
    return {"message": "Hello, this is an example route!"}
