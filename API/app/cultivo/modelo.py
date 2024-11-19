from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from .. import db
from ..tournament.modelo import Tournament


class Cultivo(db.Base):
    __tablename__ = "cultivo"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(200), nullable=False)
    tipo = Column("tipo", String(200), nullable=False)
    variedad = Column("variedad", String(200), nullable=False)
    ubicacion = Column("ubicacion", String(200), nullable=False)
    tamano = Column("tamano", String(200), nullable=False)
    fecha_cosecha = Column("fecha_cosecha", Date, nullable=False)
    tournament = relationship(Tournament)


class CultivoIn(BaseModel):
    name: str


class CultivoOut(BaseModel):
    id: int = 1
    name: str = "League of Legends"
