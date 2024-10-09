from abc import ABC, abstractmethod

# Clase abstracta TareaEmpleado
class TareaEmpleado(ABC):
    @abstractmethod
    def realizar_tarea(self):
        pass

# Clase concreta Ingeniero
class Ingeniero(TareaEmpleado):
    def realizar_tarea(self):
        return "Diseñar y supervisar proyectos de ingeniería."

# Clase concreta Doctor
class Doctor(TareaEmpleado):
    def realizar_tarea(self):
        return "Diagnosticar enfermedades y tratar a los pacientes."

# Uso de las clases
ingeniero = Ingeniero()
print(f"Tarea del ingeniero: {ingeniero.realizar_tarea()}")

doctor = Doctor()
print(f"Tarea del doctor: {doctor.realizar_tarea()}")
