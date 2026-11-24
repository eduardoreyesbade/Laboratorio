"""
NOMBRE: Eduardo Reyes
MODULO 13 - SEMAFORO

"""

class Semaforo:
    """
    Esta clase representa un semáforo sencillo.
    """
    # Constructor: Inicializa el objeto
    def __init__(self, colorIndice):
        self.indiceColores = colorIndice
        self.COLORES = ["Verde", "Amarillo", "Rojo"]

    # Método de clase: Cambia la luz de forma cíclica
    def cambiarLuz(self):
        self.indiceColores += 1
        # Si el índice se sale de la lista (0, 1, 2), vuelve a empezar
        if self.indiceColores >= len(self.COLORES):
            self.indiceColores = 0

    # Método especial: Define cómo se ve el objeto como texto
    def __str__(self):
        return self.COLORES[self.indiceColores]

# --- Uso de la Clase ---

# Creamos el primer semáforo empezando en Verde (0)
semaforo1 = Semaforo(0)

print("Estado Inicial - Semáforo 1:", semaforo1)

eleccion = ""
while eleccion != "q":     
    eleccion = input("\nPresiona Enter para cambiar el semáforo (escribe 'q' para salir): ").lower()
    
    if eleccion != "q":
        semaforo1.cambiarLuz()
        print("El Semáforo 1 ahora está en:", semaforo1)
        
        # TIP: Aquí es donde puedes añadir el código para semaforo2



# ---------- Estructura de la Clase ----------

# 1. Nombre de la Clase: ¿Cuál es el nombre de la clase en el segmento de código?
# R: Semaforo

# 2. El Constructor: ¿Cuál es el propósito de la función __init__?
# R: Inicializar los atributos

# 3. Parámetros: ¿Cuántos parámetros recibe la función __init__ (sin contar self)?
# R: 1

# 4. Atributos de Instancia: ¿Cuántas variables asociadas a self se definen en la
#    función __init__?
# R: 2


# ---------- Lógica y Comportamiento ----------

# 5. Estado Inicial: ¿Qué determina el valor inicial de self.colorIndice cuando
#    creas el objeto?
# R: El parámetro pasado al constructor

# 6. Estructura de Datos: ¿Existe alguna importancia en el orden de los colores
#    dentro de la lista self.COLORES?
# R: La secuencia de los colores y su orden. 

# 7. Cambio de Estado: Observa la función cambiarLuz. ¿Qué sucede exactamente con
#    el valor de colorIndex cada vez que se llama a esta función?
# R: le agrega 1 al indice y hace qe se mueva a la sigiuiente posicion y por ende, al seiguiente color. 

# 8. Control de Errores: ¿Qué sucede cuando el colorIndece llega a 3?
# R: El indica vuelve a 0

# 9. ¿Por qué es necesario reiniciarlo a 0?
# R: Para que el semáforo funcione en un ciclo continuo

# 10. Representación Visual: Observa la función __str__. ¿Qué determina el texto
#     que es devuelto cuando usamos print()?
# R: El color actual del semáforo

# 11. ¿Por qué está COLORES en mayúsculas?
# R:  Para indiccar que es una constate, es una convencion. 


# ---------- Uso de la Clase (Instanciación) ----------

# 12. Nombre del Objeto: ¿Cuál es el nombre de la instancia (objeto) que se crea
#     primero?
# R:  semaforo1

# 13. Interacción: Ejecuta el programa y presiona "Enter" varias veces. ¿Hay un
#     patrón en los cambios de color?
# R:  Sí, el patrón es verde, amarillo, rojo, y luego vuelve a verde.

# 14. Explícalo.
# R:  El semáforo cambia de color en un ciclo continuo segun su indice. 

# 15. Independencia: Si cambias el parámetro inicial en TrafficLight(0) por un 2,
#     ¿en qué color comenzará el semáforo?
# R:  Rojo