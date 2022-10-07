import unittest
import producto

class TestProducto(unittest.TestCase):
    def test_producto(self):
        p= producto.Producto(100, 'Jarron', 100, 'Adorno')
        self.assertEqual(p.codigo, 100)
        self.assertEqual(p.nombre, 'Jarron')
        self.assertEqual(p.precio, 100)
        self.assertEqual(p.tipo, 'Adorno')

    def test_adorno(self):
        a= producto.Adorno(200, 'Jarron', 100, 'Adorno')
        self.assertEqual(a.codigo, 200)
        self.assertEqual(a.nombre, 'Jarron')
        self.assertEqual(a.precio, 100)
        self.assertEqual(a.tipo, 'Adorno')

    def test_alimento(self):
        al= producto.Alimento(201, 'Botella de Aceite', 5, 'Alimento')
        al.productor='Los Oliveros'
        al.distribuidor= 'aceite SL'
        self.assertEqual(al.codigo, 201)
        self.assertEqual(al.nombre, 'Botella de Aceite')
        self.assertEqual(al.precio, 5)
        self.assertEqual(al.tipo, 'Alimento')
        self.assertEqual(al.productor, 'Los Oliveros')
        self.assertEqual(al.distribuidor, 'aceite SL')

    def test_rebajar_producto(self):
        al= producto.Alimento(201, 'Botella de Aceite', 5, 'Alimento')
        producto.rebajar_producto(al, 10)
        self.assertEqual(al.precio, 4.5)

    def test_menu(self):
        pass
