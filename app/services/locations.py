from app.schemas import Location


class LocationsService:
    def list(self) -> list[Location]:
        l1 = Location(
            _id="e9365041-88de-42ee-bb3e-d9a3ac71e67f",
            name="escola",
            zip_code="09700-200",
            address="rua escola",
            number="200",
            complement="sala de aula",
            contacts=["11912341234", "43514351"],
            comments="estamos recebendo tudo",
            items=[],
        )
        l2 = Location(
            _id="a4957744-83ee-42b6-b8e7-6a48ed0e9d37",
            name="faculdade",
            zip_code="09700-100",
            address="rua faculdade",
            number="100",
            complement="sala do diretor",
            contacts=["11912341234", "43514351"],
            comments="estamos recebendo tudo",
            items=[],
        )
        return [l1, l2]

    def list_one(self, id: str) -> Location:
        l2 = Location(
            name=f"faculdade {id}",
            zip_code="09700-100",
            address="rua faculdade",
            number="100",
            complement="sala do diretor",
            contacts=["11912341234", "43514351"],
            comments="estamos recebendo tudo",
            items=[],
        )
        return l2
