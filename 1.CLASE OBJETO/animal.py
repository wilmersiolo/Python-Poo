# Defino la clase
class Animal:
    # Método Constructor
    def __init__(self, nombre, tipo_animal, color):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.tipo_animal = tipo_animal
        self.color = color

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        print("Información del Animal")
        print("Nombre: " + self.nombre)
        print("Tipo de Animal: " + self.tipo_animal)
        print("Color: " + self.color)
        print("-----------------------------")

    # Método para hacer que el animal camine
    def caminar(self):
        print(f"El {self.tipo_animal} llamado {self.nombre} está caminando.")
        print("-----------------------------")

    # Método para hacer que el animal corra
    def correr(self):
        print(f"El {self.tipo_animal} llamado {self.nombre} está corriendo.")
        print("-----------------------------")

    # Método para hacer que el animal haga un sonido
    def sonar(self):
        print(f"El {self.tipo_animal} llamado {self.nombre} está haciendo un sonido.")
        print("-----------------------------")


# Creamos los objetos a partir de instanciar la clase Animal
animal1 = Animal("Burro", "Mamifero", "Gris")
animal2 = Animal("Gato", "Mamifero", "Gris")
animal3 = Animal("Perro", "Mamifero carnivoro", "Negro")

# Mostrar los detalles de cada objeto
animal1.mostrar_detalles()
animal1.caminar()
animal1.correr()
animal1.sonar()

animal2.mostrar_detalles()
animal2.caminar()
animal2.correr()
animal2.sonar()

animal3.mostrar_detalles()
animal3.caminar()
animal3.correr()
animal3.sonar()
