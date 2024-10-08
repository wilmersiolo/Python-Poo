# Clase base
class Profesionales:
    def mostrar_info(self):
        pass

    def trabajar(self):
        pass

# Clase Médico
class Medico(Profesionales):
    def __init__(self, nombre, especialidad, años_experiencia):
        self.nombre = nombre
        self.especialidad = especialidad
        self.años_experiencia = años_experiencia

    def mostrar_info(self):
        print("________________________________________________________________________________________________")
        print("Hola, soy un Doctor de la clinica santa maria")
        print(f"Nombre: Doctor. {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Años de experiencia: {self.años_experiencia}")

    def trabajar(self):
        print(f"El Doctor. {self.nombre} trabaja atendiendo pacientes.")
        print("________________________________________________________________________________________________")

# Clase Ingeniero
class Ingeniero(Profesionales):
    def __init__(self, nombre, especialidad, proyectos_realizados):
        self.nombre = nombre
        self.especialidad = especialidad
        self.proyectos_realizados = proyectos_realizados

    def mostrar_info(self):
        print("Hola, soy un ingeniero SENA")
        print(f"Nombre: Ingeniero. {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Proyectos realizados: {self.proyectos_realizados}")

    def trabajar(self):
        print(f"El Ingeniero. {self.nombre} trabaja diseñando y desarrollando proyectos de software.")
        print("________________________________________________________________________________________________")

# Clase Docente
class Docente(Profesionales):
    def __init__(self, nombre, materia, años_experiencia):
        self.nombre = nombre
        self.materia = materia
        self.años_experiencia = años_experiencia

    def mostrar_info(self):
        print("Hola, soy un profesor SENA")
        print(f"Nombre: Profesor. {self.nombre}")
        print(f"Materia: {self.materia}")
        print(f"Años de experiencia: {self.años_experiencia}")

    def trabajar(self):
        print(f"El Profesor. {self.nombre} trabaja enseñando a los estudiantes.")
        print("________________________________________________________________________________________________")

# Función que utiliza polimorfismo
def mostrar_informacion(profesional):
    profesional.mostrar_info()
    profesional.trabajar()

# Crear instancias de cada clase con atributos
medico = Medico("Juan Pérez", "Cardiología", 10)
ingeniero = Ingeniero("Ana Gómez", "Software", 15)
docente = Docente("Carlos Ruiz", "Matemáticas", 8)

# Llamar a la función con diferentes tipos de profesionales
mostrar_informacion(medico)   
mostrar_informacion(ingeniero)   
mostrar_informacion(docente)   

