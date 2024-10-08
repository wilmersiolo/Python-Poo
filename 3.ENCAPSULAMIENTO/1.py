class Personas:
    # Método constructor
    def __init__(self, nombres, apellidos, identidad, fechanacimiento, sexo):
        self._nombres = nombres  # privado (convención en Python usando _)
        self._apellidos = apellidos  # privado
        self._identidad = identidad  # privado
        self.fechanacimiento = fechanacimiento  # público
        self.sexo = sexo  # público

    # Método getter para nombres
    def obtener_nombres(self):
        return self._nombres

    # Método getter para apellidos
    def obtener_apellidos(self):
        return self._apellidos

    # Método getter para identidad
    def obtener_identidad(self):
        return self._identidad

    # Método setter para nombres
    def establecer_nombres(self, nuevo_nombres):
        self._nombres = nuevo_nombres

    # Método setter para apellidos
    def establecer_apellidos(self, nuevo_apellidos):
        self._apellidos = nuevo_apellidos

    # Método setter para identidad
    def establecer_identidad(self, nueva_identidad):
        self._identidad = nueva_identidad

    # Método para mostrar detalles del objeto
    def mostrar_detalles(self):
        return (f"Nombres: {self._nombres}\n"
                f"Apellidos: {self._apellidos}\n"
                f"N° Identidad: {self._identidad}\n"
                f"Fecha nacimiento: {self.fechanacimiento}\n"
                f"Sexo: {self.sexo}\n")


# Crear un objeto de la clase Personas
persona = Personas("Jorge", "Rojas", 1102345678, "14/09/2000", "M")

# Mostrar detalles de la persona
detalles = persona.mostrar_detalles()

# Modificar atributos encapsulados usando setters y obtenerlos con getters
persona.establecer_nombres("Carlos")  # setter
nombres = persona.obtener_nombres()  # getter
persona.establecer_apellidos("Perez")  # setter
apellidos = persona.obtener_apellidos()  # getter
identidad = persona.obtener_identidad()  # getter
fechanacimiento = persona.fechanacimiento  # público
sexo = persona.sexo  # público

detalles_modificados = f"""
Nombres: {nombres}
Apellidos: {apellidos}
N° Identidad: {identidad}
Fecha nacimiento: {fechanacimiento}
Sexo: {sexo}
"""

print(detalles)
print(detalles_modificados)
