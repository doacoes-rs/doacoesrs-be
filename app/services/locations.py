from app.schemas import Location


class LocationsService:
    def find_all(self) -> list[Location]:
        l1 = Location(
            name="escola",
            zip_code="09700-200",
            address="rua escola",
            number="200",
            complement="sala de aula",
            contacts=["11912341234", "43514351"],
            comments="estamos recebendo tudo",
            items=[]
        )
        l2 = Location(
            name="faculdade",
            zip_code="09700-100",
            address="rua faculdade",
            number="100",
            complement="sala do diretor",
            contacts=["11912341234", "43514351"],
            comments="estamos recebendo tudo",
            items=[]
        )
        return [l1, l2]
