from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_evento_db, get_all_eventos_db, get_evento_id_db
from .modelo import EventoIn, EventoOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[EventoOut],
    status_code=200,
    summary="Obtenga todos los eventos",
    description="Obtenga todos los eventos",
    operation_id="getEventos",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_eventos():
    eventos = get_all_eventos_db()
    return eventos


@router.get(
    "/{id}",
    response_model=EventoOut,
    status_code=200,
    summary="Obtenga una evento por id",
    description="Una evento sera entregado",
    operation_id="getEvento",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_evento_id(id: str):
    evento = get_evento_id_db(id)
    return evento


@router.post(
    "/",
    response_model=EventoOut,
    status_code=200,
    summary="Cree un evento",
    description="Cree un evento enviando sus datos en un JSON",
    operation_id="createEvento",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_evento(nuevo_evento: EventoIn):
    evento = create_evento_db(nuevo_evento)
    return evento
