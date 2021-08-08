'''
.:Integrantes:.

Flores Pérez Abraham Elías
Fajardo Cruz Alex Geancarlo
García Campodónico Raúl Alberto
Rivera Ruiz Joan Presley
Andrade Vera Melanie Gisella
'''

#Clase padre: esta clase se inicia con un solo item, es decir, todo este proyecto refleja una compra de un solo item por transaccion
class Producto:
    def __init__(self, item, cantidad, precioUnidad, stock, codigo, caducidad):
        self.item = item
        self.cantidad = cantidad
        self.precioUnidad = precioUnidad
        self.stock = stock
        self.codigo = codigo
        self.caducidad = caducidad



#asignamos a Producto como clase padre de la clase Usuario
class Usuario(Producto):
    def __init__(self, nombre, fechaVenta, numeroFactura, item, cantidad, precioUnidad, stock, codigo, caducidad):
        self.nombre = nombre
        self.fechaVenta = fechaVenta
        self.numeroFactura = numeroFactura
        #Importamos los parametros de la clase padre Producto
        super().__init__(item, cantidad, precioUnidad, stock, codigo, cantidad, caducidad)
    
    #Calcula el total en dolares de la compra
    def totalCompra(self):
        self.total = self.cantidad * self.precioUnidad
        return float(self.total)
    
    #Imprime la factura en un print
    def imprimirFactura(self):
        print(f'Estimado/a {self.nombre}, su total es de ${self.total} \n\n\n PRODTUCTOS:\n {self.item} x {self.cantidad} \n\n\n {self.fechaVenta} \n {self.numeroFactura}')

#asignamos a Producto como clase padre de la clase Vendedor
class Vendedor(Producto):
    def __init__(self, proveedor, fechaCompra, cantidadComprada, costo, item, cantidad, precioUnidad, stock, codigo, caducidad):
        self.proveedor = proveedor
        self.fechaCompra = fechaCompra
        self.cantidadComprada = cantidadComprada
        self.costo = costo
        #Importamos los parametros de la clase padre Producto
        super().__init__(item, cantidad, precioUnidad, stock, codigo, cantidad, caducidad)

	#Aumenta el stock de productos hasta el limite arbitrario de 500 unidades
    def restock(self):
        orden = self.stock - 500
        print(f'Se ha realizado un restock de {orden} de {self.item}')
        self.stock = orden
    
    #Cambia el proveedor del item
    def cambiarProveedor(self):
        self.proveedor = input('Porfavor escriba el proveedor que desea: ')
    
    #Imprime el stock actual del producto
    def inventario(self):
        print(f'Se encontro {self.stock} unidades de {self.item}')
