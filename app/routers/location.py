from fastapi import APIRouter, Request

router = APIRouter()


@router.get("")
def list_location(request: Request):
    return [{"id": "4e56ab83-99c3-42f4-9181-ff9de718e698"}]


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
    return {"id": id}
