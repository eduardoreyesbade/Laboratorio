#############################
# Eduardo Reyes
# 09/29/26
# M5 Tarea 1 - Seccion 4
#############################


import math

d = int(input("Ingresa la longitud de la huella de frenado (en metros): "))

# Completa la ecuación usando math.sqrt():
v = math.sqrt(2*d*10)

# Viene de la formula v = √(2 · 10 · d) = √(20·d)
# Source: Google

print("Velocidad estimada del auto:", round(v, 2), "km/h")
