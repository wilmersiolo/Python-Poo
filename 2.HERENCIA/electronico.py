class Electronico:
    # Constructor
    def __init__(self, marca, modelo, tipo_procesador):
        self.marca = marca
        self.modelo = modelo
        self.tipo_procesador = tipo_procesador
        self.capacidad_bateria = int(input("Digite la cantidad de memoria RAM: "))

    # Método público para registrar el electronico
    def registrar(self):
        print("--------------------")
        print("ELECTRÓNICO REGISTRADO")
        print("--------------------")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tipo de procesador: {self.tipo_procesador}")


class Laptop(Electronico):  # Subclase de Electronico
    # Constructor
    def __init__(self, marca, modelo, tipo_procesador, tipo_ds_duro):
        super().__init__(marca, modelo, tipo_procesador)  # Llamada al constructor de la superclase
        self.tipo_ds_duro = tipo_ds_duro
        self.duracion_de_bateria = float(input("Digite la duración de la batería en HORAS: "))

    # Método para encender el electronico
    def encender(self):
        print(f"Marca: {self.marca}")
        if self.duracion_de_bateria > 0:
            print("--------------------")
            print(f"La laptop {self.marca} modelo {self.modelo} con tipo de procesador {self.tipo_procesador} se puede encender.")
        else:
            print("--------------------")
            print(f"La laptop {self.marca}, modelo {self.modelo} con tipo de procesador {self.tipo_procesador} no se puede encender.")

# Instanciando la subclase electronico
objeto_laptop = Laptop('Lenovo', 'Lenovo IdeaPad', 'Intel Celeron N4500', 'Intel UHD Graphics')
objeto_laptop.registrar()
objeto_laptop.encender()
