    # O objeto range em Python 3 (xrange em Python 2) pode ser executado em loop como qualquer outro iterável:

for n in range(3):
    print(n)

	# E como o range é iterável, podemos obter um iterador a partir dele:

iter(range(3))
#R: <range_iterator object at 0x7fe173542ed0>

	#mas objetos range não sao 6-iteradores por si mesmos, nos nao podemos chamar next em um objeto range

next(range(3))
#R: Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# TypeError: 'range' object is not an iterator

	# E, ao contrário de um iterador, podemos fazer um loop em um objeto de intervalo sem consumi-lo:

numbers = range(3)
tuple(numbers)
#R: (0, 1, 2)
tuple(numbers)
#R:(0, 1, 2)

	# Se fizéssemos isso com um iterador, não obteríamos nenhum elemento na segunda vez em que fizemos o loop:

numbers = iter(range(3))
tuple(numbers)
#R: (0, 1, 2)
tuple(numbers)
#R:()

	# Ao contrário dos objetos zip, enumerate ou generator, os objetos range não são 6-iteradores.

	                                    #-- ENTÃO O QUE É O RANGE? --##

	# O objeto range é "lazy" em certo sentido, porque não gera todos os números que "contém" quando o criamos. Em vez
    # disso, ele nos fornece esses números conforme precisamos deles ao fazer  um loop sobre ele.

	# Aqui está um objeto range e um generator (que é um tipo de iterador):

numbers = range(1_000_000)
square = (n**2 for n in numbers)

    # Ao contrário dos 6-iteradores, os objetos range têm um comprimento(length):

len(numbers)
#R: 1000000
len(square)
#R: Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: object of type 'generator' has no len()

	# e eles podem ser indexados

numbers[-2]
# R:999998
square[-2]
# R:Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'generator' object is not subscriptable

	# E, ao contrário dos 6-iteradores, você pode perguntar se eles contêm coisas sem alterar o seu estado:

0 in numbers
True
0 in numbers
True
0 in square
True
0 in square
False

	# Se você está procurando uma descrição para objetos de alcance, pode chamá-los de “sequências lazy”. Eles são sequências (como listas,
    # tuplas e strings), mas eles realmente não contêm 		  nenhuma memória por baixo do capô e, em vez disso, respondem a perguntas
    # computacionalmente.

from collections.abc import Sequence
isinstance([1,2], Sequence)
True
isinstance('hello',Sequence)
True
isinstance(range(3),Sequence)
True

	# Se eu disser que algo é um iterador, você saberá que, ao chamá-lo, sempre obterá o mesmo objeto de volta (por definição):
my_iterator = iter([1,2,3,4])

iter(my_iterator) is my_iterator
True

	# E você terá certeza de que pode chamar next nele porque pode chamar next em todos os 6-iteradores:

next(my_iterator)
#R:4
next(my_iterator)
#R: Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#StopIteration

	# E você saberá que os itens serão consumidos do iterador à medida que você o percorre. Às vezes, esse recurso pode ser útil para
    # processar 6-iteradores de maneiras específicas:

my_iterator = iter([1, 2, 3, 4])
list(zip(my_iterator, my_iterator))
# R:[(1, 2), (3, 4)]