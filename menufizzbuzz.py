#!/usr/bin/env python
# encoding: utf-8

from os import system


class GameFizzBuzz:

    def __init__(self):
        self.fizzBuzzMenu()

    def fizzBuzzMenu(self):
        system("clear")
        print("____________________________________ Fizz Buzz _____________________________________")
        print("\nFizz -> Múltiplo de 3 | Buzz -> Múltiplo de 5 | Fizz Buzz -> Múltiplo de 3 e 5")
        print("\n____________________________________________________________________________________")

        numero = input("\nInsira um número: ")

        print ("\n----> ") + str(self.fizzBuzz(numero))

    def fizzBuzz(self, numero):

        if(numero % 3 == 0 and numero % 5 == 0):
            return "Fizz Buzz"

        if(numero % 3 == 0):
            return "Fizz"

        if(numero % 5 == 0):
            return "Buzz"
        return numero

if __name__ == '__main__':
    GameFizzBuzz()
