
"""
TODO
Crea un programa interactivo que evalúe si una persona mayor de edad está en
condiciones de conducir. Usa como referencia lo visto en la M3 Tarea de Sentencias.
Requisitos:
Entrada de datos: Solicita la edad del usuario y al menos 2 o 3 condiciones
 adicionales.
Sentencias de control: Usa estructuras condicionales (if, else if, else)
 y operadores lógicos (AND, OR, NOT) para evaluar la combinación de datos.
Salida clara: Muestra un mensaje personalizado indicando si la persona puede
 conducir o si debe entregar las llaves inmediatamente.
¡Usa tu creatividad! 
 Piensa en situaciones cómicas o extremas de la vida real.
   ¿Qué imprudencia o descuido no le permitirías a tu abuela antes de subirse al auto?
     (Ejemplo: "¿Olvidó los lentes en la cocina?")
"""

####################################
# Eduardo Reyes
# M3 - ¿Puede conducir?
####################################

print("--- EVALUACION PARA CONDUCIR ---")

# Entrada de datos
edad = int(input("¿Cuantos años tienes? "))
lentes = input("¿Traes los lenes puestos? (si/No): ").strip().lower() in ["si", "sí"]
dormido = input("¿Dormiste bien anoche? (si/no): ").strip().lower() in ["si", "sí"]
pantuflas = input("¿Vas a manjar en chalas o pantuflas? (Si/no): ").strip().lower() in ["si", "sí"]

# Evaluacion con operadores logicos
if edad < 18:
    print("NO PUEDES CONDUCIR. Todavia eres menor de edad.")

elif pantuflas:
    print("ENTREGA LAS LLAVES AHORA!. Las chalas/pantuflas resbalan en los pedales y te vas a morir!")

elif lentes and dormido:
    print("APROBADO. Puedes conducir tranquilo. Buen viaje.")

elif not lentes:
    print("NO PUEDES CONDUCIR. Tus lentes siguen en la cocina, ve por ellos.")

else:
    print("NO PUEDES CONDUCIR. Primero duerme una siesta.")


# Analysis

# ¿Cuántos commits hiciste?
# 3 en total

# ¿Qué método te pareció más fácil de usar para guardar y subir tus cambios a GitHub: los comandos en la terminal o la interfaz visual de Visual Studio Code? ¿Por qué?
# Use terminal pero el Source Control de VS Code quita menos tiempo

# ¿Para qué sirve ejecutar el comando git status antes de empezar a trabajar y cómo te ayuda a saber qué archivos han sido modificados o están pendientes por guardar?
# Para saber si hay commits que no se han subido o bajado

# ¿Por qué es fundamental descargar (git pull) los cambios más recientes del repositorio de la profesora antes de realizar y subir tus propias modificaciones al proyecto?
# Supongo por si hubo un cambio en Github y tener todo sincronizado

# En tus propias palabras, ¿cuál es la diferencia entre hacer un fork de un repositorio en GitHub y clonar (clone) un repositorio a tu computadora?
# Fork es copiar de otro usuario. Clonar es descargar  una copia en el local

# ¿Por qué es una buena práctica escribir mensajes claros y descriptivos en cada commit (por ejemplo: "Agregando mi nombre al proyecto de M4") en lugar de usar palabras vagas como "cambios" o "listo"?
# Es una buena forma de identificar que cambio en el commit que se hizo. 

# ¿Qué tipos de mensajes agregaste?
# Agregue un mensaje relativo a la parte del ejercicio que que estaba haciendo en ese instante. 

# ¿Cuál es tu sentencia preferida?
# La sentencia condicional if/ elif/else, porque permite que el programa tome decisiones dependiendo del valor dado por el usaurio

# ¿Cuándo entra el programa a la segunda sentencia de tu tarea?
# Entra al elif solo cuando la condición del if resultó False 

# ¿Qué aprendiste del README.md en tu carpeta M04? No olvides los comentarios!
# No hay.... no entendi que habia que hacer con el README.md, no se si era para escribir algo o solo para leerlo.
