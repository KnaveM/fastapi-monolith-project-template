# app/api/routes/example_route.py
from fastapi import APIRouter, Request

from app.core.rate_limit import limiter

router = APIRouter()


@router.get("/")
@limiter.limit("5/minute")
async def index(request: Request):
    return {"message": "Hello, this is the index route!"}

@router.get("/example")
async def example_route():
    return {"message": "Hello, this is an example route!"}
