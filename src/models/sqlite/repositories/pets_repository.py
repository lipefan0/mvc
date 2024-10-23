from typing import List # python 3.8
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface

class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                print(pets)
                return pets
            except NoResultFound:
                return []

    def delete_pet(self, nome: str) -> None:
        with self.__db_connection as database:
            try:
                (database.session
                    .query(PetsTable)
                    .filter(PetsTable.name == nome)
                    .delete()
                )
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
