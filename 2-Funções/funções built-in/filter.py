"""A função filter(função,lista) filtra todos os elementos de um iterável para o qual a função retorne true.
O filter precisa de uma função como seu primeiro argumento. A função precisa retornar um valor booleano. Essa função ira
aplicar a cada elemento do iterable, e somente se a função retornar True, o elemento do iterável será incluido no resultado.
OBS: se a função retornar um valor qualquer(diferente de false), será considerado True, e vai ser adicionado o elemento analisado."""
lista = [1, 2, 3, 4, 5]

def npar(n):
    if n % 2 == 0:
        return "macaco"  #True: adiciona o valor na lista
    else:
        return {}  #False: nao adiciona o valor a lista

a = list(filter(npar, lista))
b = filter(lambda x: x % 2 == 0, lista)  # a função lambda equivale a função "npar"
print(a, b)
