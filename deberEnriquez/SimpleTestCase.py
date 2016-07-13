import unittest
import Prestamo # code from module you're testing


class SimpleTestCase(unittest.TestCase):

    def setUp(self):
        """Call before every test case."""
        self.prestamo = Prestamo()
        self.valor_total = open(self, 2000, 2 )

    def tearDown(self):
        """Call after every test case."""
        self.prestamo = None

    def testA(self):
        """Test case A. note that all test method names must begin with 'test.'"""#VERIFICA para $2000 a 2 años.
        assert prestamo.valor_total(prestamo, 2000, 2) == 543, "valor_total() not calculating values correctly"

    def testB(self):
        """test case B"""
        assert prestamo.valor_total(prestamo, 8000, 4) == 543, "valor_total() not calculating values correctly"

    def testC(self):
        """test case C"""
        assert prestamo.valor_total(prestamo, 15000, 5) == 543, "valor_total() not calculating values correctly"

    def testD(self):
        """test case C"""
        assert prestamo.valor_total(prestamo, 23000, 2) == 543, "valor_total() not calculating values correctly"


if __name__ == "__main__":
    unittest.main() # run all tests