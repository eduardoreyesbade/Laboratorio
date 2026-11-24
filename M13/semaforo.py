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