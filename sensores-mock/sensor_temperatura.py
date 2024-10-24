from time import sleep
from requests import post
from random import randint


class Dispositivo:

    id: str
    key_value: str

    rango_min: float
    rango_max: float

    def __init__(self, id, key_value, rango_min, rango_max):
        self.id = id
        self.key_value = key_value
        self.rango_min = rango_min
        self.rango_max = rango_max

dispositivo_1 = Dispositivo("N0uQ4M983XqQ4TyWLIsY", "temperatura", 20, 30)
dispositivo_2 = Dispositivo("VBef7GZ68gH7cnWES15x", "humedad", 60, 100)
dispositivo_3 = Dispositivo("niwy4LHdqMtrk5B5mZVM", "precipitacion", 0, 50)

dispositivos = [dispositivo_1, dispositivo_2]


def enviar_evento(id: str, key_value: str, rango_min: float, rango_max: float):
    value = randint(rango_min, rango_max)
    post(
        f"http://localhost:8080/api/v1/{id}/telemetry",
        json={f"{key_value}": value},
    )
    print(id, key_value, value)


for iterator in range(0, 1000):
    dispositivo_1 = dispositivos[0]
    dispositivo_2 = dispositivos[1]
    enviar_evento(
        dispositivo_1.id,
        dispositivo_1.key_value,
        dispositivo_1.rango_min,
        dispositivo_1.rango_max,
    )
    enviar_evento(
        dispositivo_2.id,
        dispositivo_2.key_value,
        dispositivo_2.rango_min,
        dispositivo_2.rango_max,
    )
    enviar_evento(
        dispositivo_3.id,
        dispositivo_3.key_value,
        dispositivo_3.rango_min,
        dispositivo_3.rango_max,
    )
    sleep(1)
