# Defino la clase
class Celular:
    # Método Constructor
    def __init__(self, nombre, marca, imei, bateria, camara):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.marca = marca
        self.imei = imei
        self.bateria = bateria
        self.camara = camara

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Celular")
        print("Nombre: " + self.nombre)
        print("Marca: " + self.marca)
        print("IMEI: " + self.imei)
        print("Batería: " + str(self.bateria) + "%")
        print("Cámara: " + self.camara)
        print("-----------------------------")

    # Método para Encender el Celular
    def encender(self):
        # Evaluamos si tiene carga el celular
        if self.bateria > 0:
            print("El celular " + self.nombre + " se puede encender")
            print(f"||||||||||||| {self.bateria}% de carga")
            print("-----------------------------")
        else:
            print("El celular " + self.nombre + " no se puede encender")

# Creamos los objetos a partir de instanciar la clase Celular
celular1 = Celular("Motorola G84", "Motorola", "123456789012345", 85 , "64mpx")
celular2 = Celular("Samsung Galaxy S24", "Samsung", "234567890123456", 50, "200mpx")
celular3 = Celular("Nokia G50", "Nokia", "345678901234567", 30, "48mpx")

# Mostrar los detalles de cada objeto
celular1.mostrar_detalles()
celular1.encender()  # Método que evaluará el encendido del celular
celular2.mostrar_detalles()
celular3.mostrar_detalles()
