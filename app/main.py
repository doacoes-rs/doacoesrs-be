from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import locations

app = FastAPI()

origins = [
    "http://doacoesrs.com.br",
    "https://doacoesrs.com.br",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(locations.router, prefix="/locations")
