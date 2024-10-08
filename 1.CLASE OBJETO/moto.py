# Defino la clase
class Moto:
    # Método Constructor
    def __init__(self, nombre, marca, numero_pasajeros, numero_chasis, placa):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.numero_pasajeros = numero_pasajeros
        self.numero_chasis = numero_chasis
        self.placa = placa

    # Método para mostrar detalles de la moto
    def mostrar_detalles(self):
        print("Información de la Moto")
        print("Nombre: " + self.nombre)
        print("Marca: " + self.marca)
        print("Número de Pasajeros: " + str(self.numero_pasajeros))
        print("Número de Chasis: " + self.numero_chasis)
        print("Placa: " + self.placa)
        print("-----------------------------")
        
            # Método para Encender la moto
    def encender(self):
        print(f"La moto {self.nombre} de la marca {self.marca} está encendida.")
        print("-----------------------------")


# Creamos los objetos a partir de instanciar la clase Moto
moto1 = Moto("YZF R15", "Yamaha", 2, "1234567890ABCDE", "50AH3")
moto2 = Moto("YZ 125", "Yamaha", 1, "0987654321XYZ", "3AH64")
moto3 = Moto("KAWASAKI ZH2", "KAWASAKI", 2, "5678901234LMN", "0H15G")

# Mostrar los detalles de cada objeto
moto1.mostrar_detalles()
moto1.encender()  # Método que evaluará el encendido de la moto
moto3.mostrar_detalles()
