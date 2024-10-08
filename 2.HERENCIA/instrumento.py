class Instrumento:
    # Constructor
    def __init__(self, tipo_instrumento, marca, material_fabricacion):
        self.tipo_instrumento = tipo_instrumento
        self.marca = marca
        self.material_fabricacion = material_fabricacion
        self.precio = int(input("Digite el precio del instrumento : "))

    # Método público para registrar el dispositivo
    def registrar(self):
        print("--------------------")
        print("INSTRUMENTO REGISTRADO")
        print("--------------------")
        print(f"Tipo de instrumento: {self.tipo_instrumento}")
        print(f"Marca: {self.marca}")
        print(f"Material de fabricacion: {self.material_fabricacion}")


class Guitarra(Instrumento):  # Subclase de instrumento
    # Constructor
    def __init__(self, tipo_instrumento, marca, material_fabricacion, numero_cuerdas):
        super().__init__(tipo_instrumento, marca, material_fabricacion)  # Llamada al constructor de la superclase
        self.numero_cuerdas = numero_cuerdas
        self.acorde = input("Digite los acordes basicos de los cuales tiene conocimiento: ")

  # Método para simular tocar los acordes
    def tocar_guitarra(self):
        acordes = self.acorde
        if acordes:
            print("\nSimulando el toque de guitarra...\n")
            print("\n¡Terminaste de tocar!")
        else:
            print("No se ingresaron acordes.")

# Instanciando la subclase instrumento
objeto_instrumento = Guitarra('Acordeon', 'Cantabella', 'Madera','185 Teclas(Graves) y 45 Teclas(Agudos)')
objeto_instrumento.registrar()
objeto_instrumento.tocar_guitarra()