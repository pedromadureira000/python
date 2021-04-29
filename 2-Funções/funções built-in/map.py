"""
map() é uma função que leva dois argumentos: uma função e um objeto iteravel. Na forma map(função,iteravel)
map() aplica a função a todos os elementos da sequência(por exemplo, uma lista). Ele retorna uma nova lista com os elementos
alterados.

O objetivo do map é economizar esforço ao ter que criar manualmente loops.
"""

lista = list(range(10))

def pow(n):
    return n ** 2

lista_pow_def = list(map(pow, lista))
lista_pow_lambda = list(map(lambda n: n ** 2, lista))

a, b, c = [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]
list(map(lambda x, y, z: x + y + z, a, b, c))   #multiplos parametros e listas