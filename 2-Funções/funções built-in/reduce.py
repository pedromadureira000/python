"""A função reduce(função, sequência) aplica continuamente uma função à sequência. Em seguida, ela retorna um único valor
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates
    ((((1+2)+3)+4)+5)"""
from functools import reduce

list = [1, 2, 3, 4, 5, 6]

def teste(x, y):   #soma
    return x + y
soma = reduce(teste, list)

maior = reduce(lambda a, b: a if (a > b) else b, list)  #convere o maior

