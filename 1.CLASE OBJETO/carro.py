# Defino la clase
class Carro:
    # Método Constructor
    def __init__(self, nombre, marca, numero_pasajeros, numero_chasis, placa):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.numero_pasajeros = numero_pasajeros
        self.numero_chasis = numero_chasis
        self.placa = placa

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Carro")
        print("Nombre: " + self.nombre)
        print("Marca: " + self.marca)
        print("Número de Pasajeros: " + str(self.numero_pasajeros))
        print("Número de Chasis: " + self.numero_chasis)
        print("Placa: " + self.placa)
        print("-----------------------------")

    # Método para Encender el Carro
    def encender(self):
        print(f"El carro {self.nombre} de la marca {self.marca} está encendido.")
        print("-----------------------------")


# Creamos los objetos a partir de instanciar la clase Carro
carro1 = Carro("Chevrolet ONIX Turbo", "Chevrolet", 5, "1234567890ABCDE", "5A3BB")
carro2 = Carro("The Niro", "Kia", 9, "0987654321XYZ", "6C4AH")
carro3 = Carro("Hilux", "Toyota", 10, "5678901234LMN", "7ABCC")

# Mostrar los detalles de cada objeto
carro1.mostrar_detalles()
carro1.encender()  # Método que evaluará el encendido del carro
carro2.mostrar_detalles()
carro3.mostrar_detalles()
