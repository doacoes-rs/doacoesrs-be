from .routers import location

from fastapi import FastAPI

app = FastAPI()

app.include_router(location.router, prefix="/locations")
