from typing import Optional

from app.schemas import Location

from app.db.locationsdb import LocationsDB

db = LocationsDB()


class LocationsService:
    def list(self) -> list[Location]:
        return db.find_all()

    def list_one(self, id: str) -> Optional[Location]:
        return db.find_one(id)

    def create(self, location: Location) -> Location:
        return db.create_one(location)

    def delete(self, id: str) -> None:
        db.delete_one(id)
