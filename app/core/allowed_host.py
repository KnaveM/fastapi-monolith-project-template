# core/host_validation.py
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

class AllowedHostMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        from app.core.config import settings
        from app.api.utils import host_not_allowed
        allowed_hosts = settings.ALLOWED_HOSTS

        host = request.headers.get("host", "")
        if host not in allowed_hosts:
            _host_not_allowed = host_not_allowed.copy()
            _host_not_allowed["msg"] = f"Host {host} not allowed"
            return JSONResponse(
                    status_code=403,  # Return 403 Forbidden status code
                    content=_host_not_allowed
                    )

        response = await call_next(request)
        return response