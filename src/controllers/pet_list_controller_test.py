from src.models.sqlite.entities.pets import PetsTable
from .pet_list_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id=1, name="Fluffy", type="cat"),
            PetsTable(id=2, name="Whiskers", type="dog")
        ]

def test_list_pets():
    controller = PetListerController(MockPetsRepository())
    response = controller.list()

    expected_response = {
        "data": {
            "type": "pets",
            "count": 2,
            "attributes": [
                {
                    "name": "Fluffy",
                    "type": "cat",
                    "id": 1
                },
                {
                    "name": "Whiskers",
                    "type": "dog",
                    "id": 2
                }
            ]
        }
    }

    assert response == expected_response
