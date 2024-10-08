class Electrodomestico:
    # Constructor
    def __init__(self, marca, color, capacidad):
        self.marca = marca
        self.color = color
        self.capacidad = capacidad
        self.consumo_electrico = int(input("Digite el consumo eléctrico del electrodoméstico en (KWh): "))

    # Método público para registrar el electrodoméstico
    def registrar(self):
        print("--------------------")
        print("ELECTRODOMÉSTICO REGISTRADO")
        print("--------------------")
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Consumo eléctrico: {self.consumo_electrico} KWh")


class Refrigerador(Electrodomestico):  # Subclase de Electrodomestico
    # Constructor
    def __init__(self, marca, color, capacidad, tipo_refrigerador):
        super().__init__(marca, color, capacidad)  # Llamada al constructor de la superclase
        self.tipo_refrigerador = input("Digite el tipo de refrigerador (Frost o No Frost): ")
        self.temperatura = float(input("Digite la temperatura inicial del electrodoméstico (°C): "))

    # Método para ajustar la temperatura
    def ajustar_temp(self):
        print(f"Tipo de refrigerador: {self.tipo_refrigerador}")
        
        if self.temperatura > 32:
            print("--------------------")
            print(f"El electrodoméstico {self.marca}, con color {self.color} y capacidad {self.capacidad} tiene una temperatura adecuada y se puede encender.")
        else:
            print("--------------------")
            print(f"El electrodoméstico {self.marca}, con color {self.color} y capacidad {self.capacidad} necesita ajustar la temperatura para poder encender.")

# Instanciando la subclase electrodomestico
objeto_refrigerador = Refrigerador('Haceb', 'Rojo', '428 Lit', 'Nevera')
objeto_refrigerador.registrar()
objeto_refrigerador.ajustar_temp()
