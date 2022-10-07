import unittest
import vehiculo
import motocicleta
import coche
import camioneta
import bicicleta


class TestVehiculo(unittest.TestCase):
    def test_vehiculo(self):
        v = vehiculo.Vehiculo('rojo', 4)
        self.assertEqual(v.color, 'rojo')
        self.assertEqual(v.ruedas, 4)
        self.assertEqual(str(v), 'rojo, 4 ruedas')

class TestCoche(unittest.TestCase):
    def test_coche(self):
        c = coche.Coche('rojo', 4, 120, 1000)
        self.assertEqual(c.color, 'rojo')
        self.assertEqual(c.ruedas, 4)
        self.assertEqual(c.velocidad, 120)
        self.assertEqual(c.cilindrada, 1000)
        self.assertEqual(str(c), 'rojo, 4 ruedas, 120 km/h, 1000 cc')

class TestBicicleta(unittest.TestCase):
    def test_bicicleta(self):
        b = bicicleta.Bicicleta('azul', 2, 'urbana')
        self.assertEqual(b.color, 'azul')
        self.assertEqual(b.ruedas, 2)
        self.assertEqual(b.tipo, 'urbana')
        self.assertEqual(str(b), 'azul, 2 ruedas, urbana')

class TestCamioneta(unittest.TestCase):
    def test_camioneta(self):
        c = camioneta.Camioneta('verde', 4, 100, 1500, 500)
        self.assertEqual(c.color, 'verde')
        self.assertEqual(c.ruedas, 4)
        self.assertEqual(c.velocidad, 100)
        self.assertEqual(c.cilindrada, 1500)
        self.assertEqual(c.carga, 500)
        self.assertEqual(str(c), 'verde, 4 ruedas, 100 km/h, 1500 cc, 500 kg')

class TestMotocicleta(unittest.TestCase):
    def test_motocicleta(self):
        m = motocicleta.Motocicleta('negra', 2, 'deportiva', 200, 600)
        self.assertEqual(m.color, 'negra')
        self.assertEqual(m.ruedas, 2)
        self.assertEqual(m.tipo, 'deportiva')
        self.assertEqual(m.velocidad, 200)
        self.assertEqual(m.cilindrada, 600)
        self.assertEqual(str(m), 'negra, 2 ruedas, deportiva, 200 km/h, 600 cc')

if __name__ == '__main__':
    unittest.main()
    
