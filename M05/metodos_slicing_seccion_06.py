#############################
# Eduardo Reyes
# 09/29/26
# M5 Tarea 1 - Seccion 6
#############################

texto = input("Ingresa una frase con letras y números: ")
contador_numeros = 0

for caracter in texto:
    if caracter >= "0" and caracter <= "9":
        contador_numeros += 1

print("Total de dígitos numéricos encontrados:", contador_numeros)

# 19. Ejecuta el programa e ingresa el texto "3 tigres en 2 árboles". ¿Qué valor imprime contador_numeros? 2

# 20. Observa la condición del if. Explica cómo evalúa Python si un carácter individual es un dígito numérico usando los operadores >= y <=.
# Basicamente busca comparar cada caracter con los decimales del 0 al 9, ambos incluidos. 
