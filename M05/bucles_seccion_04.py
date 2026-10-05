#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 4: Iteración sobre Secuencias (Cadenas y Listas)
#############################    

# Iteración sobre una cadena de texto
palabra = "Python"

print("--- Letras de la palabra ---")
for letra in palabra:
    print(letra)

# Iteración sobre una lista
frutas = ["manzana", "banana", "cereza"]

print("--- Lista de frutas ---")
for fruta in frutas:
    print(fruta)

# 15. En el primer bucle for letra in palabra:, ¿qué representa la variable letra en cada paso del bucle?

# Interesante, la variable obtiene los caracteres del string

# 16. En el segundo bucle for fruta in frutas:, contrasta la iteración directa (for fruta in frutas:) con el acceso por índices (for i in range(len(frutas)):). ¿Cuál de las dos opciones resulta más legible para un principiante y por qué?

# Interesante, en este caso la variable obtiene las palabras porque es un array. Lo que hace la diferencia, es el hecho de ser un listado
