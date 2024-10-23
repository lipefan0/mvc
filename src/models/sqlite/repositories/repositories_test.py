import pytest
from src.models.sqlite.settings.connection import DBConnectionHandler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

db_connection_handler = DBConnectionHandler()

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_list_pets():
    repo = PetsRepository(db_connection_handler)
    reponse = repo.list_pets()
    print()
    print(reponse)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_delete_pet():
    name = 'Yogi'
    repo = PetsRepository(db_connection_handler)
    repo.delete_pet(name)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_insert_person():
    first_name = 'Teste Name'
    last_name = 'Teste Last Name'
    age = 30
    pet_id = 2

    repo = PeopleRepository(db_connection_handler)
    repo.insert_person(first_name, last_name, age, pet_id)

@pytest.mark.skip(reason="Interação com o banco de dados")
def test_get_person():
    person_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_person(person_id)
    print()
    print(response)
