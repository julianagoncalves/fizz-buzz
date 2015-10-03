#!/usr/bin/env python
# encoding: utf-8

def fizzBuzz(numero):

    if(numero % 3 == 0 and numero % 5 == 0):
        return "Fizz Buzz"

    if(numero % 3 == 0):
        return "Fizz"

    if(numero % 5 == 0):
        return "Buzz"

    return numero
