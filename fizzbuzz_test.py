#!/usr/bin/env python
# encoding: utf-8

import unittest
from fizzbuzz import FizzBuzz


class TestFizzBuzz(unittest.TestCase): # Caso de teste (contém vários testes)
    def test_FizzBuzz_num1(self):
        self.assertEqual(FizzBuzz(1), 1) # Verificação - O resultado de FizzBuzz(1) é igual a 1?

    def test_FizzBuzz_num2(self):
        self.assertEqual(FizzBuzz(2), 2)

    def test_FizzBuzz_num3(self):
        self.assertEqual(FizzBuzz(3), "fizz")

    def test_FizzBuzz_num4(self):
        self.assertEqual(FizzBuzz(4), 4)

    def test_FizzBuzz_num5(self):
        self.assertEqual(FizzBuzz(5), "buzz")


if __name__ == '__main__':
    unittest.main()
