from django.test import TestCase
import unittest

# Create your tests herefdsfdsfdsf.
#creando nueva pruebita
'''
from ingreso_pacientes.models import Paciente


class CrearPaciente(TestCase):

    def crear_paciente(self):
        self.paciente = Paciente.objects.create(nombres='Juan',apellidos='Vargas',cedula='0955555555')

    def test_crear_paciente(self):
        self.crear_paciente()
        self.assertIsInstance(self.paciente,Paciente,'paciente creado exitosamente')
'''
from prestamo_clase import Prestamo


class ProbarSistemaPrestamo(unittest.TestCase):

    def test_escenario1(self):
        '''CAPITAL REQUERIDO:
                CE1: [0,5000]
            TIEMPO:
                CE1: [0,3]

        '''
        nuevo_prestamo = Prestamo()
        valor = nuevo_prestamo.valor_total(prestamo=4000,tiempo=2)
        self.assertEqual(valor,4161.6)

    def test_escenario2(self):
        '''CAPITAL REQUERIDO:
                CE1: [5000,9999.99]
            TIEMPO:
                CE1: [4,6]

        '''
        nuevo_prestamo = Prestamo()
        valor = nuevo_prestamo.valor_total(prestamo=8000,tiempo=5)
        self.assertEqual(valor,8755)

    def test_escenario3(self):
        '''CAPITAL REQUERIDO:
                CE1: [10000,20000]
            TIEMPO:
                CE1: [7,12]

        '''
        nuevo_prestamo = Prestamo()
        valor = nuevo_prestamo.valor_total(prestamo=10000,tiempo=10)
        self.assertEqual(valor,11960)
                         
    def test_escenario4(self):
        '''CAPITAL REQUERIDO:
                CE4:  capital > 20000
            TIEMPO:
                CE1: [0,3]

        '''
        nuevo_prestamo = Prestamo()
        valor = nuevo_prestamo.valor_total(prestamo=21000,tiempo=2)
        self.assertEqual(valor,None)

    def test_escenario5(self):
        '''CAPITAL REQUERIDO:
                CE4: capital > 20000
            TIEMPO:
                CE2: [4,6]

        '''
        nuevo_prestamo = Prestamo()
        valor = nuevo_prestamo.valor_total(prestamo=21000,tiempo=5)
        self.assertEqual(valor,None)

    def test_escenario6(self):
        '''CAPITAL REQUERIDO:
                CE4: capital > 20000
            TIEMPO:
                CE3: [7,12]

        '''
        nuevo_prestamo = Prestamo()
        valor = nuevo_prestamo.valor_total(prestamo=21000,tiempo=10)
        self.assertEqual(valor,None)
        
