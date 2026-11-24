# ============================================================
# Módulo 12 - Mago Meteorológico (CS1400)
# Archivo: main.py  -> Menú y presentación
# Autor: Eduardo Reyes
# ============================================================

import sys

from api import obtener_clima

# En Windows la consola no usa UTF-8 por defecto y los acentos salen mal.
sys.stdout.reconfigure(encoding="utf-8")


def mostrar_bienvenida():
    """Imprime el encabezado, igual al que pide la tarea."""
    print("--- Bienvenido a Weather Wizard API ---")


def pedir_ciudad():
    """
    Pide el nombre de la ciudad y repite hasta que no venga vacío.

    Devuelve:
        str: el nombre de la ciudad, ya sin espacios de más.
    """
    # TODO 6: while True, input("Ingresa el nombre de la ciudad: ").strip()
    #         Si está vacío, avisa y continue. Si no, return.
    #         OJO: aquí NO se valida la coma. WeatherAPI acepta "Ogden" solo.
    pass


def mostrar_clima(datos):
    """
    Imprime el clima en un formato legible.

    Parámetros:
        datos (dict): la respuesta de obtener_clima().
    """
    # TODO 7: la respuesta tiene DOS bloques: "location" y "current".
    #         De location: name, region, country, localtime
    #         De current:  temp_c, feelslike_c, humidity, wind_kph
    #         El texto del clima está dos niveles adentro:
    #             datos["current"]["condition"]["text"]
    pass


def main():
    """Programa principal."""
    mostrar_bienvenida()

    ciudad = pedir_ciudad()

    # TODO 8: llamar a obtener_clima(ciudad) dentro de un try.
    #         - except ConnectionError -> imprime el error y termina.
    #         - si devuelve None -> avisa que no encontró la ciudad.
    #         - si trae datos -> mostrar_clima(datos)


if __name__ == "__main__":
    main()
