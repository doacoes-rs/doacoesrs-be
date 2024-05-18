import os
import requests
import urllib.parse
from typing import Optional

from app.schemas import Location

from app.db.locationsdb import LocationsDB

db = LocationsDB()

GOOGLE_MAPS_API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY", "")


class LocationsService:
    def list(self, state: str = None, city: str = None) -> list[Location]:
        if state or city:
            return db.find_by_state_and_city(state, city)

        return db.find_all()

    def list_one(self, id: str) -> Optional[Location]:
        return db.find_one(id)

    def create(self, location: Location) -> Location:
        coordinates = self._get_coordinates_from_google(self._build_address(location))
        location.lat = coordinates["lat"]
        location.lng = coordinates["lng"]

        return db.create_one(location)

    def delete(self, id: str) -> None:
        db.delete_one(id)

    def _build_address(self, location: Location) -> str:
        complement = f", {location.complement}" if location.complement else ""
        return f"{location.address}, {location.number}{complement}, {location.neighborhood}, {location.city}, {location.state}"

    def _get_coordinates_from_google(self, address: str) -> dict:
        try:
            response = requests.get(
                f"https://maps.googleapis.com/maps/api/geocode/json?address={urllib.parse.quote(address)}&key={GOOGLE_MAPS_API_KEY}"
            )
            response.raise_for_status()
            data = response.json()
            if len(data.get("results", [])) > 0:
                location = data["results"][0]["geometry"]["location"]
                return {"lat": location["lat"], "lng": location["lng"]}
        except Exception as e:
            print("Unable to get coordinates from Google", e)

        return {"lat": 0.0, "lng": 0.0}
