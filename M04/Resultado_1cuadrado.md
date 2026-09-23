# Analysis

Fuente: https://github.com/eduardoreyesbade/Laboratorio/blob/main/M04/1cuadrado.py

### ¿Cuántos commits hiciste?
3 en total

### ¿Qué método te pareció más fácil de usar para guardar y subir tus cambios a GitHub: los comandos en la terminal o la interfaz visual de Visual Studio Code? ¿Por qué?
Use terminal pero el Source Control de VS Code quita menos tiempo

### ¿Para qué sirve ejecutar el comando git status antes de empezar a trabajar y cómo te ayuda a saber qué archivos han sido modificados o están pendientes por guardar?
Para saber si hay commits que no se han subido o bajado

### ¿Por qué es fundamental descargar (git pull) los cambios más recientes del repositorio de la profesora antes de realizar y subir tus propias modificaciones al proyecto?
Supongo por si hubo un cambio en Github y tener todo sincronizado

### En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de un repositorio en GitHub y clonar (clone) un repositorio a tu computadora?
Fork es copiar de otro usuario. Clonar es descargar  una copia en el local

### ¿Por qué es una buena práctica escribir mensajes claros y descriptivos en cada commit (por ejemplo: "Agregando mi nombre al proyecto de M4") en lugar de usar palabras vagas como "cambios" o "listo"?
Es una buena forma de identificar que cambio en el commit que se hizo. 

### ¿Qué tipos de mensajes agregaste?
Agregue un mensaje relativo a la parte del ejercicio que que estaba haciendo en ese instante. 

### ¿Cuál es tu sentencia preferida?
La sentencia condicional if/ elif/else, porque permite que el programa tome decisiones dependiendo del valor dado por el usaurio

### ¿Cuándo entra el programa a la segunda sentencia de tu tarea?
Entra al elif solo cuando la condición del if resultó False 

### ¿Qué aprendiste del README.md en tu carpeta M04? No olvides los comentarios!
No hay....



### TODO Tarea 1: Crear una variable para almacenar el cuadrado (debe ser el numero base multiplicado por sí mismo)

cuadrado = num ** 2

### Mostrar el resultado con un f-string 

print(f"El cuadrado de {num} es: {cuadrado}")

### TODO Tarea 2, 3 y Reto : 

es_positivo = False  # Reemplaza con tu código

es_positivo = int(input("Ingresa un numero= "))

if es_positivo > 0:
    valor = True
    text = "El número es Positivo"
elif es_positivo < 0:
    valor = False
    text = "El número es Negativo"

else:
    valor = "Cero"

print(text)