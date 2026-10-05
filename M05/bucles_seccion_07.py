#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 7: Normalización de Textos con .lower()
#############################    

sujeto1 = "Python"
sujeto2 = "python"

if sujeto1.lower() == sujeto2.lower():
    print("Iguales")
else:
    print("Diferentes")

# 22. Observa las variables sujeto1 y sujeto2. ¿Cuál es la diferencia visual entre ambos textos y cuál es el resultado de la comparación inicial?
# La diferencia esta en la P, una es mayuscula y la otra esta en minuscula

# 23. Modifica la condición a if sujeto1.lower() == sujeto2.lower():. Ejecuta el código nuevamente. ¿Qué resultado obtienes y qué transformación realiza el método .lower()?
# lower() transforma los caracteres del string a minusculas.. en este caso, sujeto1 lo dejo como "python"

# 24. ¿Por qué es útil aplicar .lower() a las respuestas del usuario cuando trabajamos con entradas dentro de un bucle while (por ejemplo, al validar "SI", "Si" o "si")?
# porque si, Si, si representan basicamente el mismo valor, solo que por medio de 3 expresiones distintas. lower() have que las 3 expresiones, independiente de como se escriban, tienen una sola salida y eso evita errores de ejecucion. 
