"""
Este programa debe darle al usuario la opción de elegir una comida de una lista.
El código asegura que lo ingresado sea legible (en minúsculas) y lo compara con una lista usando lógica if/else.
Al final, muestra un mensaje explicando de dónde es originaria esa comida.
"""

# TODO #1:
# Imprime un mensaje de bienvenida al programa de comidas de Latinoamérica.

print("Bienvenido(a) al programa de comidas de Latinoamérica.")
nombre = input(("Cual es tu nombre? "))
print("Hola ", nombre)

# TODO #2:
# Muestra al usuario una lista de al menos 5 opciones de comidas para elegir.
print("Elige que deseas pedir")

# TODO #3:
# Guarda lo que el usuario escribió en una variable llamada `comida`.
# TODO #4:
# Convierte lo ingresado a minúsculas para asegurar la comparación correcta.

while True:
    comida = input("Opciones: Empanadas, Lomo Saltado, Asado, Feijoada o Bandeja Paisa? ").strip().lower()

    if comida == "empanadas":
        print("La Empanada Chilena (también conocida como empanada de pino) es el plato tradicional más emblemático de Chile, caracterizado por una masa de harina de trigo horneada o frita que envuelve un relleno jugoso de carne picada y cebolla.")
    elif comida == "lomo saltado":
        print("El Lomo Saltado es un plato tradicional de la gastronomía del Perú que consiste en un salteado de tiras de carne de res con cebolla, tomate, ají amarillo y salsa de soya, servido habitualmente con papas fritas y arroz blanco.")
    elif comida == "asado":
        print("El Asado Argentino es un ritual social y una técnica culinaria en el que se cocinan diversos cortes de carne vacuna a las brasas.")
    elif comida == "feijoada":
        print("La Feijoada es el plato nacional de Brasil, un guiso espeso, ahumado y reconfortante hecho principalmente a base de frijoles negros (alubias negras) cocidos a fuego lento con una gran variedad de carnes de cerdo y res.")
    elif comida == "bandeja paisa":
        print("La bandeja paisa es el plato típico más representativo de Colombia y el emblema de la gastronomía de la región antioqueña.")
    else:
        print("Puedes revisar tu pedido, quizas quedo mal escrito")
        continue
    break


# TODO #5:
# Usa una estructura if / elif / else para verificar la comida elegida.
# Imprime un mensaje con el país de origen para cada comida.


## Ejemplo de salida esperada:
"""
Bienvenido al programa de comidas de Latinoamérica.
Opciones: tacos, arepas, ceviche, pupusas, empanadas
¿Qué comida quieres conocer? Tacos
Los tacos son típicos de México.
"""
