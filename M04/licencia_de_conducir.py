
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
# M3 - ¿Puede conducir la abuela?
####################################

print("--- EVALUACION PARA CONDUCIR ---")

# Entrada de datos
edad = int(input("¿Cuantos años tienes? "))
lentes = input("¿Traes los lentes puestos? (si/no): ").strip().lower() in ["si", "sí"]
dormido = input("¿Dormiste bien anoche? (si/no): ").strip().lower() in ["si", "sí"]
pantuflas = input("¿Vas a manejar en pantuflas? (si/no): ").strip().lower() in ["si", "sí"]

# Evaluacion con operadores logicos
if edad < 18:
    print("NO PUEDES CONDUCIR. Todavia eres menor de edad.")

elif pantuflas:
    print("ENTREGA LAS LLAVES. Las pantuflas resbalan en los pedales.")

elif lentes and dormido:
    print("APROBADO. Puedes conducir tranquilo. Buen viaje.")

elif not lentes:
    print("NO PUEDES CONDUCIR. Tus lentes siguen en la cocina, ve por ellos.")

else:
    print("NO PUEDES CONDUCIR. Primero duerme una siesta.")
