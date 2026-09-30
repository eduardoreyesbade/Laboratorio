#############################
# Eduardo Reyes
# 09/29/26
# M5 Tarea 1 - Seccion 1
#############################

# Conteo descendente

num = int(input("Introduce el número inicial: "))

# sequence[start:stop:step]
# Source: Google
for i in range(num, 0, -1):
    print("Conteo:", i)


# 1. Ejecuta el programa e introduce 10. Al observar la consola, ¿en qué número comenzó la cuenta y en cuál terminó?
# Inicio: 10 | Fin: 1

# 2. ¿Por qué es necesario que el parámetro step (paso) sea un número negativo al realizar un conteo descendente?
# De modo que pueda sustraer dicha cantidad de la indicada por el usuario

# 3. ¿Por qué el valor final se configuró en 0 si queríamos que el conteo se detuviera en el número 1?
# Porque en STOP indicamos '0'. Si quisieramos '1' tendriamos que indicar STOP en '-1'.

# 4. Modifica el código para que cuente hacia atrás de 2 en 2, comenzando desde el número elegido por el usuario y deteniéndose exactamente en el 0 (inclusive). Escribe la línea de tu range() modificada:
#Respuesta: range( num , -2 , -2 )
