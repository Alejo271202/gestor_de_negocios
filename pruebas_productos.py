class Materia_prima:
    def __init__(self, nombre, precio,stock):
        self.nombre = nombre #nombre
        self.precio = float(precio) #precio por unidad si es peso vamos a usar gramos
        self.stock = int(stock) #cantidad de gramos
    #gastar quita stock y devuelve el precio del stock gastado
    def gastar(self, cantidad):
        self.stock = self.stock - cantidad
        return self.precio*cantidad
    #sumar añade stock y devuelve el precio del stock sumado
    def sumar(self, cantidad):
        self.stock = self.stock + cantidad
        return self.precio*cantidad
    
    def cuanto_hay(self):
        return self.stock
    #la clase Producto tiene que recibir una lista de tuplas de materias primas y cantidades usar sus precios y funciones para definir un precio propio
class Producto:
    def __init__ (self, nombre,materiales):
        self.nombre = nombre
        self.materiales = materiales
    
    def vender(self):
        precio = 0
        for material in self.materiales:
            precio = precio + material[1].gastar(material[0])
        return precio
    

plastico = Materia_prima("plastico",9,1000)
plastico2 = Materia_prima("plastico",9,1000)
electicidad = Materia_prima("electicidad",2,1000)

figura1 = Producto("figura1",[(53,plastico),(25,electicidad)])
print(f"stock de plastico {plastico.cuanto_hay()}")
print(f"stock de electicidad {electicidad.cuanto_hay()}")
print(f"stock de plastico2 {plastico2.cuanto_hay()}")
print(figura1.vender())
print(f"stock de plastico {plastico.cuanto_hay()}")
print(f"stock de electicidad {electicidad.cuanto_hay()}")
print(f"stock de plastico2 {plastico2.cuanto_hay()}")
