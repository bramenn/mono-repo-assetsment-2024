from fastapi import status
from fastapi.exceptions import HTTPException

from .. import db
from .modelo import Cultivo, CultivoIn, CultivoOut


def get_all_cultivos_db() -> CultivoOut:
    cultivos = db.session.query(Cultivo)

    if not cultivos:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cultivos no encontradas",
        )

    return [parse_cultivo(cultivo) for cultivo in cultivos]


def get_cultivo_id_db(id: str) -> CultivoOut:
    cultivo = db.session.query(Cultivo).where(Cultivo.id == id).first()

    if not cultivo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cultivo no encontrada",
        )

    return parse_cultivo(cultivo)


def create_cultivo_db(
    new_cultivo: CultivoIn,
) -> CultivoOut:
    cultivo = Cultivo(
        name=new_cultivo.name,
        tipo=new_cultivo.tipo,
        variedad=new_cultivo.variedad,
        ubicacion=new_cultivo.ubicacion,
        tamano=new_cultivo.tamano,
        fecha_siembra=new_cultivo.fecha_siembra,
        fecha_cosecha=new_cultivo.fecha_cosecha,
    )

    try:
        db.session.add(cultivo)
        db.session.commit()
        return parse_cultivo(cultivo)
    except Exception as e:
        print("No se ha creado la cultivo: ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="No se ha creado la cultivo",
        )


def parse_cultivo(cultivo: Cultivo) -> CultivoOut:
    return CultivoOut(id=cultivo.id, name=cultivo.name)
