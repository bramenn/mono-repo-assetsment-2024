from datetime import datetime
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from .. import db

from ..evento.modelo import Evento


class Cultivo(db.Base):
    __tablename__ = "cultivo"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column("name", String(200), nullable=False)
    tipo = Column("tipo", String(200), nullable=False)
    variedad = Column("variedad", String(200), nullable=False)
    ubicacion = Column("ubicacion", String(200), nullable=False)
    tamano = Column("tamano", String(200), nullable=False)
    fecha_siembra = Column("fecha_siembra", Date, nullable=False)
    fecha_cosecha = Column("fecha_cosecha", Date, nullable=False)
    tournament = relationship(Evento)


class CultivoIn(BaseModel):
    name: str
    tipo: str
    variedad: str
    ubicacion: str
    tamano: str
    fecha_siembra: datetime
    fecha_cosecha: datetime


class CultivoOut(BaseModel):
    id: int = 1
    name: str = "Lentejas"
    tipo: str = "Legumbre"
    variedad: str = "Española"
    ubicacion: str = "123;456"
    tamano: str = "25"
    fecha_siembra: datetime = datetime.now()
    fecha_cosecha: datetime = datetime.now()
