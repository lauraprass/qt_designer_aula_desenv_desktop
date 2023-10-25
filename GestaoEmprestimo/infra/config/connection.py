from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infra.config.base import Base


class DBConnectionHandler:
    def __init__(self):
        self.__connection_string = 'sqlite:///emprestimo.db'
        self.__engine = self.__create_database_engine()
        self.create_table()
        self.session = None

    def get_engine(self):
        return self.__engine

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def create_table(self):
        engine = create_engine(self.__connection_string, echo=True)
        Base.metadata.create_all(engine, checkfirst=True)


    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        print('Abrindo conexão')
        self.session = session_make
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando conexão')
        self.session.close()
