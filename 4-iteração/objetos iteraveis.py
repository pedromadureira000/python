lista = [0,1,2,3,4]
print(hasattr(lista,'__iter__')) # verifica se o objeto tem o metodo de iteração, ou seja, se ele é um iteravel
print(hasattr(lista,'__next__')) #mostra se o objeto tem o metodo next, ou seja, se ele é um iterador.



# Voce pode obter um iterador de qualquer iteravel usando a função iter():
iter([1,2])  #<list_iterator object at 0x7fe1775395f8>
iter('hello') #<str_iterator object at 0x7fe1775396a0>
# Depois de ter um iterador, a única coisa que você pode fazer com ele é obter o próximo item:
my_iterator = iter([1, 2])
next(my_iterator) #R:1
next(my_iterator) #R:2
next(my_iterator) #R:erro
# É importante observar que os iteradores têm estado. Ou seja, uma vez que você consumiu um item de um iterador, ele se foi.
# Então, depois de fazer um loop sobre um iterador uma vez, ele ficará vazio se você tentar fazer um loop novamente:
my_iterator = iter([1, 2])
print([x**2 for x in my_iterator]) #retorna: [1,4]
print([x**2 for x in my_iterator]) #na segunda vez retorna: []

'''enumerate, zip, reversed, e várias outras funções built-in retornam iteradores:'''

# Geradores (sejam de funções geradoras ou expressões geradoras) são uma das maneiras de criar seus próprios iteradores:
numbers = [1,2,3,4,5]
squares = (n**2 for n in numbers)
squares  #R: <generator object <genexpr> at 0x7fe173571258>





