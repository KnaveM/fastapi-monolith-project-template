# app/api/routes/example_route.py
from fastapi import APIRouter, Request
from fastapi_cache.decorator import cache

from app.core.rate_limit import limiter

router = APIRouter()

example_counter = 1

@router.get("/")
@limiter.limit("5/minute")
@cache(expire=60)
async def index(request: Request):
    global example_counter
    example_counter += 2
    return {"message": "Hello, this is the index route!", 'counter': example_counter}

@router.get("/example")
async def example_route():
    return {"message": "Hello, this is an example route!"}
