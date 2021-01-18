from unittest import TestCase
from POO.testes.doctest.doctestcarro import Motor

#rodando no terminal: python3 -m unittest discover foldername  (vai rodar o que começar com "test")
#rodando apenas uma porção de codigo: clique na classe pra rodar os testes da classe
                                      #clique no metodo para rodar um metodo expecifico

class Carrotest(TestCase):
    def test_velocidade_inicial(self):   #o unittest roda os metodos que começam com "test"
        motor = Motor()
        self.assertEqual(0, motor.velocidade)

    def test_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
