# ============================================================
# Módulo 12 - Mago Meteorológico (CS1400)
# Archivo: api.py  -> Conexión con WeatherAPI
# Autor: Eduardo Reyes
# ============================================================
# La API key NUNCA va escrita aquí. Se lee del archivo .env,
# que está en el .gitignore y no se sube a GitHub.

import os

import requests
from dotenv import load_dotenv

# Lee el archivo .env y mete sus valores en las variables de entorno.
load_dotenv()

URL_CLIMA = "https://api.weatherapi.com/v1/current.json"


def obtener_clima(ciudad):
    """
    Busca el clima actual de una ciudad.

    Parámetros:
        ciudad (str): el nombre de la ciudad, por ejemplo "Ogden".

    Devuelve:
        dict: los datos del clima, si los encuentra.
        None: si la ciudad no existe.

    Lanza:
        ConnectionError: si falla la red o falta la API key.
    """
    # TODO 1: leer la llave con os.getenv("WEATHER_API_KEY").
    #         Si viene None, la llave no se cargó -> lanza ConnectionError
    #         con un mensaje claro (revisa el .env).

    # TODO 2: armar los parámetros: key, q (la ciudad) y lang="es".

    # TODO 3: requests.get(URL_CLIMA, params=..., timeout=10)
    #         dentro de un try, con estos except EN ESTE ORDEN:
    #           - requests.exceptions.Timeout
    #           - requests.exceptions.HTTPError      (clave: ver TODO 4)
    #           - requests.exceptions.RequestException
    #         Los tres levantan ConnectionError con su propio mensaje.

    # TODO 4: WeatherAPI responde 400 cuando la ciudad no existe.
    #         Antes de raise_for_status(), revisa si
    #         respuesta.status_code == 400 y devuelve None en ese caso.
    #         Si no, un error del usuario se vería como error de red.

    # TODO 5: devolver respuesta.json()
    pass


# Prueba rápida: solo corre si ejecutas api.py directamente.
if __name__ == "__main__":
    import sys
    sys.stdout.reconfigure(encoding="utf-8")

    print(obtener_clima("Ogden"))
