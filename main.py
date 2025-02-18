import logging
from fastapi import FastAPI

from app import routes
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from middlewares.logger import LoggingMiddleware

logger = logging.getLogger("backend_logger")
logger.setLevel(logging.DEBUG)

app = FastAPI(
    title="Backend Server", 
    description="This is the backend server for the application", 
    version='0.0.1',
    contact= {
        "name": "Admin",
        "email": "admin@example.com"
    },
    keep_alive=True
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)

logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

handler = logging.FileHandler("backend.log")
handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logger.addHandler(handler)

@app.on_event("startup")
async def startup_event():
    '''
        This function is called when the application starts
    '''
    logger.info("Application started")

@app.on_event("shutdown")
def shutdown_event():
    '''
        This function is called when the application shuts down
    '''
    logger.warning("Application shutdown")

@app.get("/", response_class=HTMLResponse)
async def root():
    '''
        Root endpoint
    '''
    
    return """
        <html>
            <head>
                <title>Server | API</title>
            </head>
            <body>
                <h1>Go to the API Documentation</h1>
                <a href="/docs">API Documentation</a>
            </body>
        </html>
    """

app.include_router(routes.api_router)