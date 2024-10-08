# Clase base
class Animal:
    def Sonido(self):
        pass

# Clase Perro
class Perro(Animal):
    def __init__(self, raza, tamaño, edad):
        self.raza = raza
        self.tamaño = tamaño
        self.edad = edad

    def Sonido(self):
        print("________________________________________________________________________________________________")
        print("PERRO")
        print(f"Raza: {self.raza}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Edad: {self.edad} años")
        print("Sonido: ¡Guau Guau!")
        print("________________________________________________________________________________________________")

# Clase Gato
class Gato(Animal):
    def __init__(self, color, pelaje, edad):
        self.color = color
        self.pelaje = pelaje
        self.edad = edad

    def Sonido(self):
        print("GATO")
        print(f"Color: {self.color}")
        print(f"Pelaje: {self.pelaje}")
        print(f"Edad: {self.edad} años")
        print("Sonido: ¡Miau Miau!")
        print("________________________________________________________________________________________________")

# Clase Pájaro
class Pajaro(Animal):
    def __init__(self, especie, tamaño, habitat):
        self.especie = especie
        self.tamaño = tamaño
        self.habitat = habitat

    def Sonido(self):
        print("PAJARO")
        print(f"Especie: {self.especie}")
        print(f"Tamaño: {self.tamaño} cm")
        print(f"Hábitat: {self.habitat}")
        print("Sonido: ¡Pío Pío!")
        print("________________________________________________________________________________________________")

# Función que utiliza polimorfismo
def hacer_sonido(animal):
    animal.Sonido()

# Crear instancias de cada clase con atributos
perro = Perro("Labrador", "mediano", 3)
gato = Gato("blanco", "corto", 2)
pajaro = Pajaro("canario", 15, "urbano")

# Llamar a la función con diferentes tipos de animales
hacer_sonido(perro)   
hacer_sonido(gato)   
hacer_sonido(pajaro)   


 
