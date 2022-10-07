import unittest
from herencias import *

class TestHerencias(unittest.TestCase):
    def test_herencias(self):
        vehiculos=[Coche("rojo", 4, 150, 1200),Camioneta("blanco", 4, 100, 2000, 500),Bicicleta("azul", 2, "urbana"), Motocicleta('negra', 2, 'deportiva', 200, 600)]
        self.assertEqual(catalogar(vehiculos),None)
        self.assertEqual(catalogar2(vehiculos,0),None)

if __name__ == '__main__':
    unittest.main()
    