import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Middleware class
class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Log request path
        print(f"Request URL: {request.url.path}")

        # Record start time
        start_time = time.time()

        # Call the next middleware or endpoint
        response = await call_next(request)

        # Record end time and calculate processing time
        process_time = time.time() - start_time

        # Add time in response headers
        response.headers["X-Process-Time"] = str(process_time)

        return response
