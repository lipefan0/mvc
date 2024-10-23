from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = "sqlite:///storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self):
        if self.__engine is None:
            self.__engine = create_engine(self.__connection_string)

    def get_engine(self):
        if self.__engine is None:
            self.connect_to_db()
        return self.__engine

    def __enter__(self):
        self.connect_to_db()
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

db_connection_handler = DBConnectionHandler()
