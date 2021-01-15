# Sets (ou conjuntos) são coleções desordenadas de elementos únicos.
lista = list(range(10))
conj = set(lista) #transforma uma lista em conjunto
a,b = {1, 2, 3, 4},{3, 4, 5, 6}   #define um conjunto
print(a.union(b))    #retorna a união entre o conjunto """"a"""" e o conjunto """"b""
print(a.intersection(b))
l1,l2= [1,2,3],[2,3,4]
print(set(l1).intersection(l2))#transforma em conjunto a lista ""l1"" e faz a intersecção com a #lista""l2""
print(a.intersection_update(b)) #faz a intersecção entre ""a"" e ""b"" e atribui o resultado a ""a""
print(a.difference(b))  #retorna a diferença
print(a.symmetric_difference(b)) #retorna todos os elementos (de ambos os conjuntos a e #b) que pertencem a somente um dos conjuntos.
print(a.issubset(b))   #verifica se ""a"" é subconjunto de ""b""
print(a.isdisjoint(b)) #verifica se os conjuntos são disjuntos. Dois conjuntos são disjuntos #se tiverem interseção nula.
lista = list(set(lista)) #transforma lista em set e set em lista novamente.                                                                          ########################Modificações de conjuntos##########################
conj.add(9)  #adiciona elemento ao conjunto
conj.update(['rai', 'roi']) #adiciona novos elementos
conj.remove('roi')  # se n ouver o elemento dará erro
conj.discard('rui')  # se n ouver n da erro
del conj  #deleta o conjunto
conj.clear()  #limpa os elemntos do conjunto"