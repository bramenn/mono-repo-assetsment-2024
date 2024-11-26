from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Evento, EventoIn, EventoOut, EventosOut


def get_all_eventos_db() -> EventoOut:
    eventos = db.session.query(Evento)

    if not eventos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Eventos no encontrados",
        )

    return [parse_evento(evento) for evento in eventos]


def get_eventos_cultivo_id_db(id: str) -> EventosOut:
    eventos = db.session.query(Evento).where(Evento.cultivo_id == id)

    if not eventos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Eventos no encontrados",
        )

    return [parse_evento(evento) for evento in eventos]


def get_evento_id_db(id: str) -> EventoOut:
    evento = db.session.query(Evento).where(Evento.id == id).first()

    if not evento:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento no encontrado",
        )

    return parse_evento(evento)


def create_evento_db(
    new_evento: EventoIn,
) -> EventoOut:
    evento = Evento(
        titulo=new_evento.titulo,
        descripcion=new_evento.descripcion,
        nivel=new_evento.nivel,
        fecha_evento=new_evento.fecha_evento,
    )

    try:
        db.session.add(evento)
        db.session.commit()
        return parse_evento(evento)
    except Exception as e:
        print("No se ha creado el evento: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado el evento",
        )


def parse_evento(evento: Evento) -> EventoOut:
    return EventoOut(
        id=evento.id,
        titulo=evento.titulo,
        descripcion=evento.descripcion,
        nivel=evento.nivel,
        fecha_evento=evento.fecha_evento,
    )
