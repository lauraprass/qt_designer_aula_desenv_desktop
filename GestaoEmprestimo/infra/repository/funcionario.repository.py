from datetime import datetime
from sqlalchemy.orm import joinedload

from infra.config.connection import DBConnectionHandler
from infra.entities.funcionario import Funcionario
from infra.entities.uniforme import Uniforme
from infra.entities.emprestimo import Emprestimo


class EmprestimoRepository:
    @staticmethod
    def insert_emprestimo(funcionario, uniforme):
        with DBConnectionHandler as db:
            emp = Emprestimo()
            emp.uniforme_id = uniforme.id
            emp.funcinario_id = funcionario.id
            today = datetime.now()
            emp.data_emprestimo = datetime.strftime(today, '%d/%m/%Y %H:%M:%S')

            try:
                db.session.add(emp)
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def finalize_emprestimo(funcionario, uniforme):
        with DBConnectionHandler as db:
            today = datetime.now()
            try:
                db.session.query(Emprestimo).filter(
                    Emprestimo.uniforme_id == uniforme.id,
                    Emprestimo.funcinario_id == funcionario.id).update({'data_devolucao': today})
                db.session.commit()
            except Exception as e:
                print(e)

    @staticmethod
    def select_all_emprestimos():
        with DBConnectionHandler as db:
            emprestimos = db.session.query(Emprestimo).options(joinedload(Emprestimo.funcinario),
                                                                joinedload(Emprestimo.uniforme)).all()
            return emprestimos

    @staticmethod
    def delete_emprestimo(emprestimo):
        with DBConnectionHandler as db:
            db.session.delete(emprestimo)
            db.session.commit()

    @staticmethod
    def select_emprestimos_ativos():
        with DBConnectionHandler as db:

            emprestimos = (db.session.query(Emprestimo, Funcionario, Uniforme)
                           .join(Funcionario, Funcionario.id == Emprestimo.funcionario_id)
                           .join(Uniforme, Uniforme.id == Emprestimo.uniforme_id)
                           .filter(Emprestimo.data_devolucao.is_(None)))
            return emprestimos

    @staticmethod
    def select_emprestimos_in_period(begin_date, end_date):
        try:
            begin_date_ = datetime.strptime(begin_date, '%d/%m/%Y %H:%M:%S')
            end_date_ = datetime.strptime(end_date, '%d/%m/%Y %H:%M:%S')
            end_date_ = end_date_.replace(hour=23, minute=59, second=59)
            with DBConnectionHandler as db:
                emprestimos = (
                    db.session.query(Emprestimo, Funcionario, Uniforme)
                    .join(Funcionario, Funcionario.id == Emprestimo.funcionario_id)
                    .join(Uniforme, Uniforme.id == Emprestimo.uniforme_id)
                    .filter(Emprestimo.data_emprestimo.between(begin_date_, end_date_))
                    .options(
                        joinedload(Emprestimo.funcinario),
                        joinedload(Emprestimo.uniforme))
                    .all()
                )
                return emprestimos
        except Exception as e:
            print(e)