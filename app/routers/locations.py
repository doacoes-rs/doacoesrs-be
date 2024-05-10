from http import HTTPStatus
from typing import Optional, List

from fastapi import APIRouter, Response

from app.schemas import Location
from app.services import LocationsService

router = APIRouter()

service = LocationsService()


@router.get("")
def list_location(
    page: int = 0, state: str = None, city: str = None
) -> Optional[List[Location]]:
    return service.list()


@router.post("")
def create_location(location: Location) -> Location:
    return service.create(location)


@router.patch("/{id}")
def update_location(Location: Location) -> Location:
    return {}


@router.delete("/{id}", responses={204: {}})
def delete_location(id: str) -> None:
    service.delete(id)
    return Response(status_code=HTTPStatus.NO_CONTENT)


@router.get("/{id}")
def location(id: str) -> Optional[Location]:
    location = service.list_one(id)
    if not location:
        return Response(status_code=HTTPStatus.NOT_FOUND)

    return location
