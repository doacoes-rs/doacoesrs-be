from fastapi import FastAPI

from .routers import location

app = FastAPI()

app.include_router(location.router, prefix="/locations")
