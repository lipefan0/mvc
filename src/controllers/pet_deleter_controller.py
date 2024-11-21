from src.models.sqlite.repositories.pets_repository import PetsRepository

class PetDeleterController:
    def __init__(self, __pet_repository: PetsRepository):
        self.__pet_repository = __pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pet(name)
