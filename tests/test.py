import unittest
import deuda

class TestMethods(unittest.TestCase):

    def test_inferior5000(self):
        capital = deuda.valor_total(2000, 2)
        self.assertEqual(capital, 2080.8)

    def test_mayor20000(self):
        capital = deuda.valor_total(22000, 6)
        self.assertEqual(capital, None)

    def test_inferior10000(self):
        capital = deuda.valor_total(8000, 4)
        self.assertEqual(capital, 8652)

    def test_inferior20000(self):
        capital = deuda.valor_total(18000, 7)
        self.assertEqual(capital, 20685.6)

if __name__ == '__main__':
    unittest.main()
