from http import HTTPStatus

from fastapi import APIRouter, Response

from app.schemas import Location
from app.services import LocationsService

router = APIRouter()

service = LocationsService()


@router.get("")
def list_location() -> list[Location]:
    return service.list()


@router.post("")
def create_location(Location: Location) -> Location:
    return {}


@router.patch("")
def update_location(Location: Location) -> Location:
    return {}


@router.delete("/{id}", responses={204: {}})
def delete_location(id: str) -> None:
    return Response(status_code=HTTPStatus.NO_CONTENT)


@router.get("/{id}")
def location(id: str) -> Location:
    return service.list_one(id)
