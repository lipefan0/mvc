from typing import Dict, List
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.repositories.pets_repository import PetsRepository

class PetListerController:
    def __init__(self, __pet_repository: PetsRepository):
        self.__pet_repository = __pet_repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.format_response(pets)
        return response

    def __get_pets_in_db(self) -> List[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def format_response(self, pets: List[PetsTable]) -> Dict:
        formatted_pets = []
        for pet in pets:
            formatted_pets.append({
                "name": pet.name,
                "type": pet.type,
                "id": pet.id
            })

        return {
            "data": {
                "type": "pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }
