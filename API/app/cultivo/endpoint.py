from typing import List

from fastapi import APIRouter

# from .consultas import 
from .modelo import CultivoIn, CultivoOut

router = APIRouter()

@router.get(
    "/",
    response_model=List[CultivoOut],
    status_code=200,
    summary="Obtenga todos los viewers",
    description="Multiples viewers seran entregados en una lista de json, separados por comas ",
    operation_id="getViewers",
    responses={404: {"model": CultivoIn}},
)
def get_all_viewers():
    pass