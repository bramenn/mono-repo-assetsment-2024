from typing import List

from fastapi import APIRouter

from ..responses.http import _404NotFound, _500ServerError
from .consultas import create_cultivo_db, get_all_cultivos_db, get_cultivo_id_db
from .modelo import CultivoIn, CultivoOut

router = APIRouter()


@router.get(
    "/",
    response_model=List[CultivoOut],
    status_code=200,
    summary="Obtenga todos los cultivos",
    description="Obtenga todos los cultivos",
    operation_id="getCultivos",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_all_cultivos():
    cultivos = get_all_cultivos_db()
    return cultivos


@router.get(
    "/{id}",
    response_model=CultivoOut,
    status_code=200,
    summary="Obtenga una cultivo por id",
    description="Una cultivo sera entregado",
    operation_id="getCultivo",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def get_cultivo_id(id: str):
    cultivo = get_cultivo_id_db(id)
    return cultivo


@router.post(
    "/",
    response_model=CultivoOut,
    status_code=200,
    summary="Cree un cultivo",
    description="Cree un cultivo enviando sus datos en un JSON",
    operation_id="createCultivo",
    responses={404: {"model": _404NotFound}, 500: {"model": _500ServerError}},
)
def create_cultivo(nuevo_cultivo: CultivoIn):
    cultivo = create_cultivo_db(nuevo_cultivo)
    return cultivo
