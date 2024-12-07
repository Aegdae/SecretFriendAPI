from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Grupo(Base):
    __tablename__ = "grupo"
    grupo_id = Column(Integer, primary_key=True)
    grupo_name = Column(String(255))
    participantes = relationship(
        "Participante", back_populates="grupo", cascade="all, delete-orphan"
    )

class Participante(Base):
    __tablename__ = "participantes"
    part_id = Column(Integer, primary_key=True)
    part_name = Column(String(255))
    grupo_id = Column(Integer, ForeignKey("grupo.grupo_id"))
    grupo = relationship("Grupo", back_populates="participantes")