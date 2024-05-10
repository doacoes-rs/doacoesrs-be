import uuid
from typing import List

from app.schemas import Location
from . import DB

data: List[Location] = [
    Location(
        id="e9365041-88de-42ee-bb3e-d9a3ac71e67f",
        name="escola",
        zip_code="09700-200",
        address="rua escola",
        number="200",
        complement="sala de aula",
        contacts="11912341234",
        comments="estamos recebendo tudo",
        city="Sao Paulo",
        state="SP",
        items=[],
        expiration_date=1715304177,
    ),
    Location(
        id="a4957744-83ee-42b6-b8e7-6a48ed0e9d37",
        name="faculdade",
        zip_code="09700-100",
        address="rua faculdade",
        number="100",
        complement="sala do diretor",
        contacts="11912341234",
        comments="estamos recebendo tudo",
        city="Sao Paulo",
        state="SP",
        items=[],
        expiration_date=1715304177,
    ),
]


class InMemoryDB(DB):
    def find_all(self):
        return data

    def find_one(self, id: str):
        for d in data:
            if d.id == id:
                return d

        return None

    def delete_one(self, id: str):
        for d in data:
            if d.id == id:
                data.remove(d)
                break

    def update_one(self, id: str, model: any):
        for d in data:
            if d.id == id:
                data.remove(d)
                data.append(model)
                return d
        pass

    def create_one(self, model: any):
        model.id = uuid.uuid4()
        data.append(model)
        return model
