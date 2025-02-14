
class producto:

    def __init__self,id, nombre, cantidad, precio):
    self._id = id
    self._nombre = nombre
    self._cantidad = cantidad
    self._precio = precio

    # getters
    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @property
    def cantidad(self):
        return self._cantidad

    @property
    def precio(self):
        return self._precio

    #setters
    def cantidad(self, nueva cantidad):
    self._ cantidad =nuevo cantidad

    @precio.setter
    def precio(self, nuevo_precio):
        self._precio = nuevo nuevo_precio

    def __str__(self):
        return f"ID: {self._id}, Nombre: {self._nombre}, cantidad: {self._ cantidad}, precio:{self._precio}"

    class inventario:
    def __init__(self):
        self.producto = []

        def agregar_producto(self, producto):
            if any(p.id == producto.id for p in self.productos):
                raise valueError("EL ID del producto ya existe.")
            self.productos.append(producto)

        def eliminar _producto(self, id):
            self.producto = [p for p in self.producto if p.id != id]

        def actualizar_producto(self,id, cantidad=None, precio=None):
            for producto in self.productos:
                if producto.id == id:
                    if cantidad is not None:
                        producto.cantidad = cantidad
                    if precio is not None:
                        producto.precio = precio
                        return
                    raise ValueError("producto no encontrado.")

                def buscar_producto(self, nombre):
                    retur [p for p in self.productos if nombre.lower() in p.nombre.lower()]

                def mostrar_inventario(self):
                    for producto in self.productos:
                        print(producto)

     # crear inventario
        inventario = inventario()

    # crear productos
    producto1 = producto(1, "manzana", 50, 0.5)
    producto2 = producto(2, "platano", 30, 0.2)

    # agregar producto al inventario
    inventario.agregar_producto(producto1)
    inventario.agregar_producto(producto2)

    # mostrar inventario
    print("inventario despues de agregar producto:")
    inventario.mostrar_inventario()

    # actualizar un producto
    print("\nBuscar producto 'manzana':")
    productos_encontrados = inventario.buscar_producto("manzana")
    for p in productos_encontrados:
        print(p)

    # eleiminar un producto
    inventario. eleiminar_producto(2)

    # mostrar inventario despues de la eliminacion
    print("\nInventario despues de eliminar un producto:")
    inventario.mostrar_inventario()








