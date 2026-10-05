#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 3: Bucle for y la Función range() (Iteración Definida)
#############################    

# Ejemplo de range() simple
num = int(input("Introduce un número límite: "))

for i in range(2,11,2):
    print("Iteración:", i)

# 8. Ejecuta el programa e ingresa el valor 10. ¿Cuántas veces se imprimió la palabra "Iteración"? ¿Influyó en algo el número ingresado por teclado en este primer intento?

# 10 veces siempre porque el 10 esta hardcoded

# 9. Observa la salida numéricas de i. ¿Cuál es el valor inicial y cuál es el valor final impreso?

# Valor inicial:0

# Valor final: 02

# 10. ¿Se llegó a imprimir el número 10 en la consola? Explica por qué Python excluye el límite superior en range().

# no, porque al incluir el 0, el rango impreso ya tiene 10 salidas

# 11. Cambia range(10) por range(0, 10). ¿Existe alguna diferencia en el resultado obtenido?

# no

# IMPORTANTE: range(start, stop[, step])

# 12. Ejecuta e ingresa 20. ¿El conteo se detuvo en 20 o en 19?

# en 19

# 13. ¿Qué ajuste matemático debes hacer dentro de range() para que la cuenta incluya exactamente el número ingresado por el usuario?

# que al stop le agregue un numero extra: 1,num+1


# 14. Ejecuta el programa. ¿Qué valores se imprimieron y qué función cumple el tercer argumento dentro de range(inicio, fin, paso)?

# Para 20: 2, 4, 6, 8, 10... 11 todo esta hardcoded
