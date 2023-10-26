from __future__ import annotations
from typing import List
from sqlalchemy import Column, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from infra.config.base import Base


class Funcionario(Base):
    __tablename__ = 'funcionarios'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome: Mapped[str] = mapped_column(nullable=False)
    cpf: Mapped[str] = mapped_column(nullable=False, unique=True)
    ativo: Mapped[bool] = mapped_column(default=True, nullable=False)
    emprestimos = relationship("Emprestimo", back_populates="funcionario", cascade="save-update")


    def __repr__(self):
        return f'Funcionario [nome= {self.nome}, cpf={self.cpf}]'