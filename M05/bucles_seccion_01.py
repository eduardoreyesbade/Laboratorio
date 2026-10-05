#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 1: ¿Por qué usar un Bucle? (Repetición Manual vs. Iteración)
#############################

# Impresión manual repetitiva
# print("Hola, estudiante")
# print("Hola, estudiante")
# print("Hola, estudiante")
# print("Hola, estudiante")
# print("Hola, estudiante")

# 1. Si quisieras saludar a 100 estudiantes, ¿qué problema presenta el enfoque mostrado en el Código 1?
# que es muy lento y puedo haber un error al escribirlo

# 2. ¿Crees que este enfoque manual permite adaptar el número de saludos dinámicamente si el usuario lo solicita en tiempo de ejecución? Explica por qué.
# Si es posible. De la siguiente forma
"""
nombres =  ["Eduardo", "Carlos", "Chris"]

for nombre in nombres:
    print("Hola, ",nombre)
"""

# Intento de repetición con if

respuesta = input("¿Deseas repetir el proceso? (si/no): ").lower()

if respuesta == "si":
    print("Ejecutando el bloque...")
    respuesta = input("¿Deseas repetir el proceso? (si/no): ")

print("Programa finalizado.")

