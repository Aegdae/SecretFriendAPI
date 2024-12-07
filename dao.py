from sqlalchemy import select
from secretdb import Database_engine
from entidade import Grupo, Participante
from sqlalchemy.orm import Session

session = Session(Database_engine)

class GrupoDAO:
    def obterTodos(self):
        return session.query(Grupo).all()
    def obter(self, grupo_id):
        return session.get(Grupo, grupo_id)
    def incluir(self, grupo):
        session.add(grupo)
        session.commit()
    def excluir(self, grupo_id):
        grupo = session.get(Grupo, grupo_id)
        if grupo:
            session.delete(grupo)
            session.commit()


class ParticipanteDAO:
    def obterTodos(self):
        stmt = select(Participante)
        result = session.execute(stmt)
        return result.scalars().all()
    def obterTodosGrupo(self, grupo_id):
        stmt = select(Participante).where(Participante.grupo_id == grupo_id)
        result = session.execute(stmt)
        return result.scalars().all()
    def incluir(self, participante):
        session.add(participante)
        session.commit()
    def excluir(self, participante_id):
        participante = session.get(Participante, participante_id)
        if participante:
            session.delete(participante)
            session.commit()