# app/main.py
from fastapi import FastAPI
from debug_toolbar.middleware import DebugToolbarMiddleware
import logging
from slowapi.errors import RateLimitExceeded
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from app.core.config import settings
from app.core.logging import setup_logging
from app.api.routes import ws as websocket_route, example as example_route
from app.core.rate_limit import limiter, rate_limit_exceeded_handler

app = FastAPI(title=settings.API_TITLE, version=settings.API_VERSION, debug=settings.DEBUG)

setup_logging()

if settings.DEBUG:
    logging.info("Debug mode: ON")
    app.add_middleware(
        DebugToolbarMiddleware,
        # panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
    )
    # patch self.router.url_path_for("debug_toolbar.render_panel")

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.include_router(websocket_route.router)
app.include_router(example_route.router)

@app.on_event("startup")
async def startup():
    redis_client = aioredis.from_url(settings.REDIS_URL, encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")