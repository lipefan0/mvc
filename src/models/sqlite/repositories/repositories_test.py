import pytest
from src.models.sqlite.settings.connection import DBConnectionHandler
from .pets_repository import PetsRepository

db_connection_handler = DBConnectionHandler()

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    reponse = repo.list_pets()
    print()
    print(reponse)

def test_delete_pet():
    name = 'Yogi'
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name)
