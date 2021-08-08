
#Grupo#25

class Item: #Clase item que se usará para crear el objeto producto
    nombre = ""
    codigo = 0
    valorunit = 0.00
    caducidad = ""
    fecha_compra = ""
    proveedor = ""
    stock = 0
    costo_comprado = 0

    def __init__(self,n,co,vU,cad,fcom,prov,stk): #Inicializa con los campos correspondientes
        self.nombre = n
        self.codigo = co
        self.valorunit = vU
        self.caducidad = cad
        self.fecha_compra = fcom
        self.proveedor = prov
        self.stock = stk

    def dismistock(self,numero): #baja un valor al stock que tiene el item
        self.stock -= numero

    def aumentstock(self,numero,cstcom): #sube un valor al stock que tiene el item y almacena su costo comprado
        self.stock+=numero
        self.costo_comprado = cstcom

class Cliente: #Clase cliente que se usará para crear el objeto comprador
    nombre = ""
    lista_productos = []
    pago = 0

    def __init__(self, n): #inicializa colocando el nombre como parametro
        self.nombre = n

    def agregar_producto(self,nombre_producto): #agrega el nombre del producto a una lista de productos
        self.lista_productos.append(nombre_producto)

    def deuda(self,costo): #aumenta su deuda por cada costo ingresado
        self.pago+=costo

class Factura: #Clase factura que se usará para crear el objeto registro
    fechaVenta = ""
    numeroFactura = ""
    def __init__(self, fcv, numf): #inicializa con valores de la fechaVenta y el numero de factura
        self.fechaVenta = fcv
        self.numeroFactura = numf

    def compraproducto(self,cliente,nomprd,listitems,cantidad): #modifica el valor de pago al comprar un producto
        for item in listitems:
            if nomprd == item.nombre:
                costo = cantidad * item.valorunit
                cliente.deuda(costo)