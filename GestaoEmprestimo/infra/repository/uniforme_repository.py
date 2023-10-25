from infra.config.connection import DBConnectionHandler
from infra.entities.uniforme import Uniforme

class UniformeRepository:

    @staticmethod
    def select_uniforme_by_id(id_uniforme):
        with DBConnectionHandler as db:
            uniforme = db.session.query(Uniforme)\
                .filter(Uniforme.id == id_uniforme).first()
            return uniforme

    @staticmethod
    def select_uniforme_by_name(name_uniforme):
        with DBConnectionHandler as db:
            uniforme = db.session.query(Uniforme)\
                .filter(Uniforme.nome == name_uniforme).first()
            return uniforme

    @staticmethod
    def select_all_uniformes():
        with DBConnectionHandler as db:
            uniformes = db.session.query(Uniforme).all()
            return uniformes

    @staticmethod
    def select_first_uniforme():
        with DBConnectionHandler as db:
            uniforme = db.session.query(Uniforme).first()
            return uniforme

    @staticmethod
    def insert_many_uniformes(uniformes):
        with DBConnectionHandler as db:
            if isinstance(uniformes, list):
                db.session.query(Uniforme).add_all(uniformes)
                db.session.commit()
            else:
                print(uniformes)

    @staticmethod
    def insert_one_uniformes(uniforme):
        with DBConnectionHandler as db:
            db.session.query(Uniforme).add(uniforme)
            db.session.commit()


    @staticmethod
    def delete_uniforme(uniforme):
        with DBConnectionHandler as db:
            db.session.query(Uniforme).filter(Uniforme.id == uniforme.id)\
                .update({'ativo': False})
            db.session.commit()