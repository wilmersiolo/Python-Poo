# Clase base
class InstrumentosMusicales:
    def Tocar(self):
        pass

# Clase Piano
class Piano(InstrumentosMusicales):
    def __init__(self, tipo, num_teclas):
        self.tipo = tipo
        self.num_teclas = num_teclas

    def Tocar(self):
        print("____________________________________________________________________________________________________________________")
        print("PIANO")
        print(f"Tipo: {self.tipo}")
        print(f"Número de teclas: {self.num_teclas}")
        print("Sonido: ¡Tú tú tú!")
        print("____________________________________________________________________________________________________________________")

# Clase Guitarra
class Guitarra(InstrumentosMusicales):
    def __init__(self, tipo, num_cuerdas):
        self.tipo = tipo
        self.num_cuerdas = num_cuerdas

    def Tocar(self):
        print("GUITARRA")
        print(f"Tipo: {self.tipo}")
        print(f"Número de cuerdas: {self.num_cuerdas}")
        print("Sonido: ¡Strum strum!")
        print("____________________________________________________________________________________________________________________")

# Clase Batería
class Bateria(InstrumentosMusicales):
    def __init__(self, tipo, num_tambores):
        self.tipo = tipo
        self.num_tambores = num_tambores

    def Tocar(self):
        print("BACTERIA")
        print(f"Tipo: {self.tipo}")
        print(f"Número de tambores: {self.num_tambores}")
        print("Sonido: ¡Boom boom!")
        print("____________________________________________________________________________________________________________________")

# Función que utiliza polimorfismo
def hacer_sonido(instrumento):
    instrumento.Tocar()

# Crear instancias de cada clase con atributos
piano = Piano("piano de cola", 88)
guitarra = Guitarra("guitarra acústica", 6)
bateria = Bateria("batería electrónica", 5)

# Llamar a la función con diferentes tipos de instrumentos
hacer_sonido(piano)   
hacer_sonido(guitarra)   
hacer_sonido(bateria)   

