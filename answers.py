#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 1
# Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

def exercise_1(input_list=[]):
    squared_list = list(map(lambda x: x * x, input_list))
    print(squared_list)        # [2, 4, 6, 8, 10]
    cubed_list = list(map(lambda x: x * x * x, input_list))
    print(cubed_list)        # [2, 4, 6, 8, 10]

# Ejercicio 2
# Write a Python class to implement pow(x, n)

class Pow(object):
    """docstring for Pow"""
    def __init__(self, x, n):
        super(Pow, self).__init__()
        self.x = x
        self.n = n

    def pow_(self):
        return pow(self.x, self.n)

# Ejercicio 3
# Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda.
# Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.
# Escriba un programa que indique si el número ingresado es o no palíndromo

def is_palindrome( s ):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome( s[1:-1] )
        else:
            return False

def main():
    exercise_1(input_list=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    print(f"Pow(2, 3) = {Pow(2, 3).pow_()}")
    print(f"Pow(5, 2) = {Pow(5, 2).pow_()}")

    num = 123
    print(f" Is palindrome {num} ? {'yes' if is_palindrome(str(num)) else 'no'}")

    num = 323
    print(f" Is palindrome {num} ? {'yes' if is_palindrome(str(num)) else 'no'}")


if __name__ == "__main__":
    main()

