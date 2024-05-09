from fastapi import FastAPI

from app.routers import locations

app = FastAPI()

app.include_router(locations.router, prefix="/locations")
