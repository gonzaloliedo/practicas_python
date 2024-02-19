#video 2 Herencia, Polimorfismo y sobrecarga de métodos

class Producto:                         #clase padre
    def __init__(self, id, descripcion, costo):
        self.id = id
        self.descripcion = descripcion
        self.costo = costo

    def crear_etiquetas(self):
        return " %s \n %s \n %0.2f \n" % (self.id, self.descripcion, self.costo)
    
class Perecedero (Producto):                        #clase hija
    def __init__(self, id, descripcion, costo, fecha_caducidad):
        super().__init__(id, descripcion, costo)    #apuntador a la clase padre
        self.fecha_caducidad = fecha_caducidad

    def crear_etiquetas(self):                      # se sobrecarga el método crear_etiqueta para que también imprima la fecha de caducidad
        return super().crear_etiquetas() + "%s \n" % self.fecha_caducidad

class Electronico (Producto):
    def __init__(self, id, descripcion, costo, marca):
        super().__init__(id, descripcion, costo)    #apuntador a la clase padre
        self.marca = marca

producto = Producto("159623", "producto generico", 200.00)
comida = Perecedero("159785", "jitomate", 10.00, "18/02/2024")
electronico = Electronico("789123", "Lavadora", 2000.00, "Samsung")

# por herencia no es necesario escribir de nuevo el método crear_etiquetas
"""
print(producto.crear_etiquetas())
print(comida.crear_etiquetas())
print(electronico.crear_etiquetas())
"""
objetos = (producto, comida, electronico)

for objeto in objetos:
    print(objeto.crear_etiquetas(), type(objeto)) # el objeto está adoptando diferentes formas en cada iteración, puede ser un producto genérico, un percedero o un electrónico (POLIMORFISMO)