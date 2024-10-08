# Clase base Vehiculo
class Vehiculo:
    def Descripcion(self):
        pass

# Clase Carro
class Carro(Vehiculo):
    def __init__(self, marca, año, transmision):
        self.marca = marca
        self.año = año
        self.transmision = transmision

    def Descripcion(self):
        print("________________________________________________________________________________________________")
        print("CARRO")
        print(f"Marca: {self.marca}")
        print(f"Año: {self.año}")
        print(f"Transmisión: {self.transmision}")
        print("________________________________________________________________________________________________")

# Clase Moto
class Moto(Vehiculo):
    def __init__(self, marca, tipo_motor, potencia):
        self.marca = marca
        self.tipo_motor = tipo_motor
        self.potencia = potencia

    def Descripcion(self):
        print("MOTO")
        print(f"Marca: {self.marca}")
        print(f"Tipo de motor: {self.tipo_motor}")
        print(f"Potencia: {self.potencia} HP")
        print("________________________________________________________________________________________________")

# Clase Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, tipo, tamaño_rueda, velocidades):
        self.tipo = tipo
        self.tamaño_rueda = tamaño_rueda
        self.velocidades = velocidades

    def Descripcion(self):
        print("BICICLETA")
        print(f"Tipo: {self.tipo}")
        print(f"Tamaño de rueda: {self.tamaño_rueda} pulgadas")
        print(f"Velocidades: {self.velocidades}")
        print("________________________________________________________________________________________________")

# Función que utiliza polimorfismo
def mostrar_informacion_vehiculo(vehiculo):
    vehiculo.Descripcion()

# Crear instancias de cada clase con atributos
carro = Carro("Tesla", 2023, "automática")
moto = Moto("Ducati", "bicilíndrico", 150)
bicicleta = Bicicleta("urbana", 29, 21)

# Llamar a la función con los nuevos vehículos
mostrar_informacion_vehiculo(carro)      
mostrar_informacion_vehiculo(moto)       
mostrar_informacion_vehiculo(bicicleta)





