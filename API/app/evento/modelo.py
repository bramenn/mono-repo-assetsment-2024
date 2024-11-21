from datetime import datetime
from enum import Enum as PyEnum

from pydantic import BaseModel, Field
from sqlalchemy import Column, Date, Enum, Integer, String
from sqlalchemy.sql.schema import ForeignKey

from .. import db


class NivelEnum(PyEnum):
    CRITICO = "critico"
    ALTO = "alto"
    MEDIO = "medio"
    BAJO = "bajo"

class Evento(db.Base):
    __tablename__ = "evento"
    id = Column("id", Integer, autoincrement=True, primary_key=True, unique=True)
    titulo = Column("titulo", String(200), nullable=False)
    descripcion = Column("descripcion", String(400), nullable=False)
    nivel = Column("nivel", Enum(NivelEnum), nullable=False)
    fecha_evento = Column("fecha_evento", Date, nullable=False)

    cultivo_id = Column(Integer, ForeignKey("cultivo.id"))


class EventoIn(BaseModel):
    titulo: str
    descripcion: NivelEnum = Field(..., description="Nivel del evento: critico, alto, medio, bajo")
    nivel: str
    fecha_evento: datetime

    cultivo_id: int


class EventoOut(BaseModel):
    id: str = 1
    titulo: str = "Plaga detectada"
    descripcion: str = "Una plaga se a detectado en tu zona"
    nivel: NivelEnum = NivelEnum.CRITICO
    fecha_evento: datetime = datetime.now()

    cultivo_id: int = 10
