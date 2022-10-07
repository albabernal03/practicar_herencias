import unittest
import producto

class TestProducto(unittest.TestCase):
    def test_producto(self):
        self.assertEqual(producto.producto(2, 3), 6)
        self.assertEqual(producto.producto(2, 0), 0)
        self.assertEqual(producto.producto(2, 1), 2)
        self.assertEqual(producto.producto(2, -1), -2)
        self.assertEqual(producto.producto(2, -3), -6)

if __name__ == '__main__':
    unittest.main()
    