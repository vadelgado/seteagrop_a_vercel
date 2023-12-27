# application/perros/models/entities/productos.py

class productos:
    def __init__(self, ProductoID, Nombre, CategoriaID, Precio, Descripcion, Imagen):
        self.ProductoID = ProductoID
        self.Nombre = Nombre
        self.CategoriaID = CategoriaID
        self.Precio = Precio
        self.Descripcion = Descripcion
        self.Imagen = Imagen

