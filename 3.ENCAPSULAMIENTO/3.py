class Libro:
    # Método constructor
    def __init__(self, titulo, autor, editorial):
        self._titulo = titulo  # privado
        self._autor = autor  # privado
        self.editorial = editorial  # público

    # Método getter para título
    def obtener_titulo(self):
        return self._titulo

    # Método getter para autor
    def obtener_autor(self):
        return self._autor

    # Método setter para título
    def establecer_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo

    # Método setter para autor
    def establecer_autor(self, nuevo_autor):
        self._autor = nuevo_autor

    # Método para mostrar detalles del libro
    def mostrar_detalles(self):
        return (f"Título: {self._titulo}\n"
                f"Autor: {self._autor}\n"
                f"Editorial: {self.editorial}\n")


# Crear un objeto de la clase Libro
libro = Libro("Cien años de soledad", "Gabriel García Márquez", "Editorial Sudamericana")

# Mostrar detalles del libro
detalles_libro = libro.mostrar_detalles()

# Modificar atributos encapsulados usando setters y obtenerlos con getters
libro.establecer_titulo("El amor en los tiempos del cólera")  # setter
titulo = libro.obtener_titulo()  # getter
libro.establecer_autor("Gabriel García Márquez")  # setter
autor = libro.obtener_autor()  # getter
editorial = libro.editorial  # público

detalles_modificados = f"""
Título: {titulo}
Autor: {autor}
Editorial: {editorial}
"""

print(detalles_libro)
print(detalles_modificados)
