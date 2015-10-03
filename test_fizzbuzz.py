#!/usr/bin/env python
# encoding: utf-8

import unittest
from fizzbuzz import *
teste = GameFizzBuzz()

class TestFizzBuzz(unittest.TestCase): # Caso de teste (contém vários testes)
    def test_FizzBuzz_simples(self):
        self.assertEqual(teste.fizzBuzz(1), 1) # Verificação - O resultado de FizzBuzz(1) é igual a 1?
        self.assertEqual(teste.fizzBuzz(2), 2)
        self.assertEqual(teste.fizzBuzz(4), 4)

    def test_FizzBuzz_multiplos_de_3(self):
        self.assertEqual(teste.fizzBuzz(3), "Fizz")
        self.assertEqual(teste.fizzBuzz(9), "Fizz")

    def test_FizzBuzz_multiplos_de_5(self):
        self.assertEqual(teste.fizzBuzz(5), "Buzz")
        self.assertEqual(teste.fizzBuzz(10), "Buzz")

    def test_FizzBuzz_multiplos_de_3_e_5(self): 
        self.assertEqual(teste.fizzBuzz(15), "Fizz Buzz")


if __name__ == '__main__':
    unittest.main()
