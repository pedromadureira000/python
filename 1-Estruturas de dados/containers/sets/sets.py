# Sets (ou conjuntos) são coleções desordenadas de elementos únicos.

    #criar sets
conj = set(range(10))  # transforma em conjunto
a, b = {1, 2, 3, 4}, {3, 4, 5, 6}  # define um conjunto

    #união
print(a.union(b))  # retorna a união entre o conjunto "a" e o conjunto "b"

    #intersecção
a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
print(a.intersection(b))
l1, l2 = [1, 2, 3], [2, 3, 4]
print(set(l1).intersection(l2))

    #verificar diferença
a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
print(a.difference(b))  # retorna a diferença de "a" com "b" (a-b)
print(a.symmetric_difference(b))  # retorna todos os elementos (de ambos os conjuntos a e b) que pertencem a somente um dos conjuntos.

    #verificar de subconjunto e disjunção
a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
print(a.issubset(b))  # verifica se "a" é subconjunto de "b" (retorna um bool)
print(a.isdisjoint(b))  # verifica se os conjuntos são disjuntos. Se tem interseção nula. (retorna um bool)                                                                   ########################Modificações de conjuntos##########################

    #atualizar conjuntos
a, b = {1, 2, 3, 4}, {3, 4, 5, 6}
print(a.intersection_update(b))  # faz a intersecção entre "a" e "b" e atribui o resultado a "a"
conj.add(9)  # adiciona elemento ao conjunto
conj.update(['rai', 'roi'])  # adiciona novos elementos
conj.remove('roi')  # se n ouver o elemento dará erro
conj.discard('rui')  # se n ouver n da erro
conj.clear()  # limpa os elemntos do conjunto"
del conj  # deleta o conjunto

    #set comprehension
x = {s for s in [1, 2, 1, 0, "oi", "", True, False]}
print(type(x), x)