class Producto:
    # Método constructor
    def __init__(self, nombre, precio, cantidad, categoria):
        self._nombre = nombre  # privado
        self._precio = precio  # privado
        self.cantidad = cantidad  # público
        self.categoria = categoria  # público

    # Método getter para nombre
    def obtener_nombre(self):
        return self._nombre

    # Método getter para precio
    def obtener_precio(self):
        return self._precio

    # Método setter para nombre
    def establecer_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    # Método setter para precio
    def establecer_precio(self, nuevo_precio):
        self._precio = nuevo_precio

    # Método para mostrar detalles del producto
    def mostrar_detalles(self):
        return (f"Nombre: {self._nombre}\n"
                f"Precio: {self._precio}\n"
                f"Cantidad: {self.cantidad}\n"
                f"Categoría: {self.categoria}\n")


# Crear un objeto de la clase Producto
producto = Producto("Laptop", 1500, 20, "Electrónica")

# Mostrar detalles del producto
detalles_producto = producto.mostrar_detalles()

# Modificar atributos encapsulados usando setters y obtenerlos con getters
producto.establecer_nombre("Laptop Gamer")  # setter
nombre = producto.obtener_nombre()  # getter
producto.establecer_precio(1800)  # setter
precio = producto.obtener_precio()  # getter
cantidad = producto.cantidad  # público
categoria = producto.categoria  # público

detalles_modificados = f"""
Nombre: {nombre}
Precio: {precio}
Cantidad: {cantidad}
Categoría: {categoria}
"""

# Imprimir los detalles
print(detalles_producto)
print(detalles_modificados)
