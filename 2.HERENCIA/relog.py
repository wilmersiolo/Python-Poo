class Relog:
    # Constructor
    def __init__(self, marca, material):
        self.marca = marca
        self.material = material
        self.precio = int(input("Digite el precio del reloj: "))

    # Método público para registrar el reloj
    def registrar(self):
        print("--------------------")
        print("RELOJ REGISTRADO")
        print("--------------------")
        print(f"Marca: {self.marca}")
        print(f"Material: {self.material}")
        print(f"Precio: {self.precio}")


class Relog_inteligente(Relog):  # Subclase de reloj
    # Constructor
    def __init__(self, marca, material, tipo_pantalla):
        super().__init__(marca, material)  # Llamada al constructor de la superclase
        self.tipo_pantalla = tipo_pantalla
        self.sistema_operativo = input("Digite el sistema operativo (ejemplo: Wear OS): ")

    # Método para encender el reloj
    def encender(self):
        respuesta = input("¿Deseas encender el reloj? (si/no): ")
        if respuesta.lower() == "si":
            print(f"El reloj {self.marca}, de material {self.material} con tipo de pantalla {self.tipo_pantalla} se está encendiendo.")
        else:
            print(f"El reloj {self.marca}, de material {self.material} con tipo de pantalla {self.tipo_pantalla} no se puede encender.")


# Instanciando la subclase Relog_inteligente
objeto_relog = Relog_inteligente('Apple', 'Titanio', 'OLED')
objeto_relog.registrar()
objeto_relog.encender()
