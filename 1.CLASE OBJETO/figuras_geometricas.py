# Defino la clase
class FiguraGeometrica:
    # Método Constructor
    def __init__(self, nombre, forma, numero_lados, angulo, area):
        # Defino los atributos de instancia de la clase
        self.nombre = nombre
        self.forma = forma
        self.numero_lados = numero_lados
        self.angulo = angulo
        self.area = area

    # Método para mostrar detalles de la figura geométrica
    def mostrar_detalles(self):
        print("Información de la Figura Geométrica")
        print("Nombre: " + self.nombre)
        print("Forma: " + self.forma)
        print("Número de Lados: " + str(self.numero_lados))
        print("Ángulo: " + str(self.angulo) + "°")
        print("Área: " + str(self.area) + " unidades cuadradas")
        print("-----------------------------")


# Creamos los objetos a partir de instanciar la clase FiguraGeometrica
figura1 = FiguraGeometrica("Triángulo ", "Triángulular", 3, 80, 5.0)
figura2 = FiguraGeometrica("Cuadrado", "Cuadrada", 4, 90, 13.0)
figura3 = FiguraGeometrica("Pentágono Regular", "Pentágono", 4, 11, 13.5)

# Mostrar los detalles de cada objeto
figura1.mostrar_detalles()
figura2.mostrar_detalles()
figura3.mostrar_detalles()
