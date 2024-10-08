# Defino la clase
class Empleado:
    # Método Constructor
    def __init__(self, nombre, trabajo, peso, estatura, edad):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.trabajo = trabajo
        self.peso = peso
        self.estatura = estatura
        self.edad = edad

    # Método para mostrar detalles del empleado
    def mostrar_detalles(self):
        print("Información del Empleado")
        print("Nombre: " + self.nombre)
        print("Trabajo: " + self.trabajo)
        print("Peso: " + str(self.peso) + " kg")
        print("Estatura: " + str(self.estatura) + " m")
        print("Edad: " + str(self.edad) + " años")
        print("-----------------------------")

# Creamos los objetos a partir de instanciar la clase Empleado
empleado1 = Empleado("Maria peñate rivera", "Enfermera", 51, 1.72, 32)
empleado2 = Empleado("Wilmer berrio siolo", "Desarrollador de software", 50, 1.67, 20)
empleado3 = Empleado("Claudia paricia montes", "Odontologa", 51, 1.65, 37)

# Mostrar los detalles de cada objeto
empleado1.mostrar_detalles()
empleado2.mostrar_detalles()
empleado3.mostrar_detalles()
