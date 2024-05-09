from fastapi import APIRouter, Request

from app.schemas import Location
from app.services import LocationsService

router = APIRouter()

service = LocationsService()


@router.get("")
def list_location(request: Request) -> list[Location]:
    return service.list()


@router.post("")
def create_location(request: Request):
    return {}


@router.patch("")
def update_location(request: Request):
    return {}


@router.delete("/{id}")
def delete_location(request: Request, id: str):
    return {}


@router.get("/{id}")
def location(request: Request, id: str):
    return service.list_one(id)
