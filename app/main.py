# app/main.py
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import setup_logging
from app.api.routes import ws as websocket_route, example as example_route
from debug_toolbar.middleware import DebugToolbarMiddleware
import logging

app = FastAPI(title=settings.API_TITLE, version=settings.API_VERSION, debug=settings.DEBUG)

setup_logging()

if settings.DEBUG:
    logging.info("Debug mode: ON")
    app.add_middleware(
        DebugToolbarMiddleware,
        # panels=["debug_toolbar.panels.sqlalchemy.SQLAlchemyPanel"],
    )
    # patch self.router.url_path_for("debug_toolbar.render_panel")



app.include_router(websocket_route.router)
app.include_router(example_route.router)