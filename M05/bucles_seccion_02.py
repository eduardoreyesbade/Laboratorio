#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 2: Bucle while (Iteración Indefinida)
#############################

# Intento de repetición con if
"""
respuesta = input("¿Deseas repetir el proceso? (si/no): ").lower()

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")
"""
# 3. Ejecuta el programa e introduce "si" en la primera pregunta y "si" en la segunda. ¿El programa preguntó una tercera vez o finalizó? Explica por qué sucede esto usando un if.

# No pregunto una tercera vez porque el segundo if esta anidado dentro de un if que ya se ejecuto. Habria que introducir un while probablemenye

# 4. Ejecuta el programa e ingresa "si" varias veces consecutivas. ¿Cómo cambia el comportamiento respecto al if?
"""
respuesta = input("¿Deseas repetir el proceso? (si/no): ").lower()

while respuesta == "si":
    print("Ejecutando el bloque...")

print("Programa finalizado.")
"""
# se ejecuta infinitamente

# 5. ¿Es posible saber con exactitud de antemano cuántas veces el usuario escribirá "si" antes de ejecutar el programa?

# No, no es posible


# respuesta = input("¿Deseas repetir el proceso? (si/no): ").lower()

while respuesta == "si":
    print("Ejecutando el bloque...")

print("Programa finalizado.")

# 6. ¿Qué le sucede al programa cuando no se actualiza la variable de control dentro del while?

# No se ejecuta, esta esperando el input de la variable respuesta

# 7. Investiga qué combinación de teclas se utiliza en la terminal para detener un bucle infinito en ejecución (Ctrl+C u otra). Escríbela.

# siempre he usado Ctrl + C
