#############################
# Eduardo Reyes
# 10/03/26
# M5 Laboratorio sobre Iteración 
#############################
# Sección 5: Sentencias de Control de Bucles (break y continue)
#############################    

# Uso de break y continue
print("Demostración de continue:")
for num in range(1, 6):
    if num == 3:
        continue
    print("Número:", num)

print("\nDemostración de break:")
for num in range(1, 6):
    if num == 3:
        break
    print("Número:", num)

# 17. Observa la salida de la Demostración de continue. ¿Qué número falta en la secuencia impresa y por qué ocurrió esto?
# El contimue crea una especie de "excepcion"

# 18. Observa la salida de la Demostración de break. ¿Qué números se imprimieron y qué hace la instrucción break al ejecutarse?
# El break corta de raiz la ejecucion del loop

# 19. Supón que construyes un bucle while True: para solicitar claves de acceso. ¿Qué sentencia te permitiría salir del bucle una vez que el usuario ingrese la clave correcta?
# creo que el break, porque el continue sigue con el loop
