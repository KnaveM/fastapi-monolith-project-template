# core/rate_limit.py
from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from starlette.responses import JSONResponse, Response
from starlette.requests import Request

from app.api.utils import rate_limit_exceeded

limiter = Limiter(key_func=get_remote_address)

def rate_limit_exceeded_handler(request: Request, exc: RateLimitExceeded) -> Response:
    """
    Build a simple JSON response that includes the details of the rate limit
    that was hit. If no limit is hit, the countdown is added to headers.
    """
    response = JSONResponse(rate_limit_exceeded, status_code=429)
    response = request.app.state.limiter._inject_headers(
        response, request.state.view_rate_limit
    )
    return response
