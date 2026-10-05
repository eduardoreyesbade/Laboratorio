#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 6: Patrones de Acumulación y Conteo
#############################    

# Acumulador de suma y contador de coincidencias
numeros = [4, 7, 2, 9, 10, 5]
suma_total = 0
mayores_a_cinco = 0

for num in numeros:
    suma_total += num  # Acumula la suma
    if num > 5:
        mayores_a_cinco += 1  # Incrementa el contador



print("Suma total:", suma_total)
print("Cantidad de números mayores a 5:", mayores_a_cinco)

# 20. ¿Con qué valor deben inicializarse las variables suma_total y mayores_a_cinco antes de comenzar el bucle? ¿Qué pasaría si las inicializas dentro del bucle?
# Con cero, para asegurarnos que no tengan una cifra. Ahora, tienen que declararse antes de ejecutar el loop, dentro o despues, no funciona, entra en error como 'no definidas'

# 21. Explica con tus palabras la diferencia entre un acumulador (suma_total += num) y un contador (mayores_a_cinco += 1).
# Un acumulador es la funcion que hace la sumatoria y el otro cuenta literalmente el numero de datos que cumplen con la condiicion. 

