from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import logging


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Log Middleware")
        logging.info(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        logging.info(f"Response: {response.status_code}")
        return response
