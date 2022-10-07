class Producto:
    def __init__(self,codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    def __str__(self):
        return'''\
            CODIGO\t{}
            NOMBRE\t{}
            PRECIO\t{}
            TIPO\t{}'''.format(self.codigo, self.nombre, self.precio, self.tipo)

class Adorno(Producto): #hereda de producto y va a tener todos sus atributos iguales
    pass

a= Adorno(200, 'Jarron', 100, 'Adorno')
print(a)
print('El producto se ha creado con exito')

class Alimento(Producto):
    productor=''
    distribuidor=''

al= Alimento(201, 'Botella de Aceite', 5, 'Alimento')
al.productor='Los Oliveros'
al.distribuidor= 'aceite SL'
