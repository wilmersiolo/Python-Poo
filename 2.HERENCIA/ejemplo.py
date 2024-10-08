class Vehiculo:
    # constructor
    def __init__(self, marca, color, modelo):
        self.marca = marca
        self.color = color
        self.modelo = modelo
        self.numero_llantas = int(input("No. de Llantas:"))

    # métodos públicos
    def registrar(self):
        print("--------------------")
        print("CARRO REGISTRADO")
        print("--------------------")
        print("Marca: ", self.marca)
        print("Color: ", self.color)
        print("Modelo: ", self.modelo)
        print("No. de Llantas: ", self.numero_llantas)


class Carro(Vehiculo):  # subclase Carro
    # constructor
    def __init__(self, marca, color, modelo, placa):
        super().__init__(marca, color, modelo)  # super clase heredada
        self.placa = placa  # atributo privado
        self.gasolina = int(input("No. de Galones de Gasolina: "))

    # método privado
    def encender(self):
        print("Placa: ", self.placa)  # imprimiendo la placa

        if self.gasolina > 0:
            print("--------------------")
            print(f"El carro {self.marca}, con placa {self.placa} de color {self.color} enciende!!")
        else:
            print("--------------------")
            print(f"El carro {self.marca}, con placa {self.placa} de color {self.color} no enciende!!")


# instanciando la subclase carro
objeto_carro = Carro('SUZUKI', 'Rojo', '2022', 'PPC 54C')
objeto_carro.registrar() 