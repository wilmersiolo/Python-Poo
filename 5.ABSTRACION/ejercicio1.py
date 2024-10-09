
from abc import ABC, abstractmethod

# Clase abstracta Empleado
class Empleado(ABC):
    @abstractmethod
    def calcular_salario(self):
        pass


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, salario_mensual):
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        return self.salario_mensual


class EmpleadoPorHoras(Empleado):
    def __init__(self, horas_trabajadas, tarifa_por_hora):
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

# Uso de las clases
empleadoTiempoC = EmpleadoTiempoCompleto(400000)
print(f"Salario del empleado de tiempo completo: {empleadoTiempoC.calcular_salario()}")

empleadoPorH = EmpleadoPorHoras(4800, 15)
print(f"Salario del empleado por horas: {empleadoPorH.calcular_salario()}")
