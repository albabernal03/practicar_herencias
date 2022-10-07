class Producto:
    def __init__(self,codigo, nombre, precio, tipo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.tipo = tipo
    print('El producto se ha creado con exito')
    def __str__(self):
        return'''\
            CODIGO\t{}
            NOMBRE\t{}
            PRECIO\t{}
            TIPO\t{}'''.format(self.codigo, self.nombre, self.precio, self.tipo)

class Adorno(Producto): #hereda de producto y va a tener todos sus atributos iguales
    pass

a= Adorno(200, 'Jarron', 100, 'Adorno')



class Alimento(Producto):
    productor=''
    distribuidor=''

al= Alimento(201, 'Botella de Aceite', 5, 'Alimento')
al.productor='Los Oliveros'
al.distribuidor= 'aceite SL'


productos= [a, al]
for p in productos:
    print(p,'\n')

def rebajar_producto(p, rebaja):
    '''Devuelve el producto con la rebaja aplicada'''
    p.precio= p.precio -(p.precio/100 * rebaja)
aplica_rebaja= rebajar_producto(al, 10)
print(aplica_rebaja)
print(al)