import json
import uuid
from datetime import datetime

from app.gcp import get_bigquery_client
from app.schemas import Location

from . import DB


class LocationsDB(DB):
    def __init__(self) -> None:
        super().__init__()
        self.client = get_bigquery_client()
        self.table = "abiding-splicer-422816-i4.doacoesrs.locations"

    def find_all(self):
        job = self.client.query(f"SELECT * FROM {self.table}")
        rows = job.result()
        locations = []
        for row in rows:
            locations.append(self.read_row(row))
        return locations

    def find_by_state_and_city(self, state: str, city: str):
        query = f"SELECT * FROM {self.table}"

        filters = []

        if state:
            filters.append(f"state = '{state}'")

        if city:
            filters.append(f"city = '{city}'")

        if filters:
            where = " AND ".join(filters)
            query += f" WHERE {where}"

        job = self.client.query(query)
        rows = job.result()
        locations = []
        for row in rows:
            locations.append(self.read_row(row))
        return locations

    def find_one(self, id: str):
        job = self.client.query(f"SELECT * FROM {self.table} WHERE id = '{id}'")
        rows = job.result()
        for row in rows:
            return self.read_row(row)

    def delete_one(self, id: str):
        job = self.client.query(f"DELETE FROM {self.table} WHERE id = '{id}'")
        job.result()
        return id

    def update_one(self, id: str, model: any):
        job = self.client.query(
            f"UPDATE {self.table} SET name = '{model.name}' WHERE id = '{id}'"
        )
        job.result()
        return model

    def create_one(self, model: any):
        model.id = uuid.uuid4()
        expiration_date = datetime.fromtimestamp(model.expiration_date)
        create_date = datetime.fromtimestamp(model.create_date)
        items = json.dumps([item.value for item in model.items])
        job = self.client.query(
            f"""
            INSERT INTO {self.table}
                (
                    id, name, zip_code, address, neighborhood, number, city, state, complement, contacts, comments, expiration_date, items, create_date
                )
            VALUES
                (
                    '{model.id}',
                    '{model.name}',
                    '{model.zip_code}',
                    '{model.address}',
                    '{model.neighborhood}',
                    '{model.number}',
                    '{model.city}',
                    '{model.state}',
                    '{model.complement}',
                    '{model.contacts}',
                    '{model.comments}',
                    '{expiration_date}',
                    PARSE_JSON('{items}'),
                    '{create_date}'
                )"""
        )
        job.result()
        return model

    def read_row(self, row):
        return Location(
            id=row.id,
            name=row.name,
            zip_code=row.zip_code,
            address=row.address,
            number=row.number,
            complement=row.complement,
            contacts=row.contacts,
            comments=row.comments,
            city=row.city,
            state=row.state,
            neighborhood=row.neighborhood or "",
            items=row.get("items"),
            expiration_date=row.expiration_date.timestamp(),
            create_date=row.create_date.timestamp(),
        )
