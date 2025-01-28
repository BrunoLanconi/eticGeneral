from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
import logging


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Auth Middleware")
        if not request.headers.get("Authorization"):
            return JSONResponse(status_code=401, content={"message": "Unauthorized"})

        # Do something with the Authorization header

        response = await call_next(request)
        return response


class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Log Middleware")
        logging.info(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        logging.info(f"Response: {response.status_code}")
        return response


class ErrorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print("Error Middleware")

        try:
            response = await call_next(request)
            return response
        except Exception as e:
            return JSONResponse(
                status_code=500, content={"message": "Internal Server Error"}
            )
