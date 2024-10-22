from sqlalchemy import Column, BIGINT, String
from src.models.sqlite.settings.base import Base

class PeopleTable(Base):
    __tablename__ = 'people'

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    pet_id = Column(BIGINT, nullable=False)
