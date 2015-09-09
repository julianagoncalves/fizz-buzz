#!/usr/bin/env python
# encoding: utf-8

import unittest
from fizzbuzz import FizzBuzz 


class TestFizzBuzz(unittest.TestCase): # Caso de teste (contém vários testes)
    def test_FizzBuzz(self):
        self.assertEqual(FizzBuzz(1), 1) # Verificação - O resultado de FizzBuzz(1) é igual a 1?


if __name__ == '__main__':
    unittest.main()
