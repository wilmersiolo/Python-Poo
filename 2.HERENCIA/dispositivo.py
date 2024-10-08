class Dispositivo:
    # Constructor
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.capacidad_bateria = int(input("Digite la capacidad de la batería del dispositivo (mAh): "))

    # Método público para registrar el dispositivo
    def registrar(self):
        print("--------------------")
        print("DISPOSITIVO REGISTRADO")
        print("--------------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Capacidad de la batería del dispositivo: {self.capacidad_bateria} mAh")


class Smartphone(Dispositivo):  # Subclase de dispositivo
    # Constructor
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)  # Llamada al constructor de la superclase
        self.sistema_operativo = input("Digite el sistema operativo del smartphone (iOS o Android): ")
        self.conectividad = input("Digite el tipo de conectividad del smartphone (4G o 5G): ")

    # Método para encender el smartphone
    def encender(self):
        print(f"Sistema operativo: {self.sistema_operativo}")
        
        if self.capacidad_bateria > 0:
            print("--------------------")
            print(f"El smartphone {self.marca}, modelo {self.modelo} del año {self.año} se puede encender.")
        else:
            print("--------------------")
            print(f"El smartphone {self.marca}, modelo {self.modelo} del año {self.año} no se puede encender debido a falta de batería.")

# Instanciando la subclase Smartphone
objeto_smartphone = Smartphone('Samsung', 'Galaxy S24 Ultra', '2024')
objeto_smartphone.registrar()
objeto_smartphone.encender()

