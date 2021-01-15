# O objeto range em Python 3 (xrange em Python 2) pode ser executado em loop como qualquer outro iterável:

for n in range(3):
    print(n)

	# E como o range é iterável, podemos obter um iterador a partir dele:

iter(range(3))
# R:<range_iterator object at 0x7fe173542ed0>

	# mas objetos range não sao 6-iteradores por si mesmos, nos nao podemos chamar next em um objeto range

next(range(3))
# R:Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'range' object is not an iterator

	# E, ao contrário de um iterador, podemos fazer um loop em um objeto de intervalo sem consumi-lo:

numbers = range(3)
tuple(numbers)
# R:(0, 1, 2)
tuple(numbers)
# R:(0, 1, 2)

	# Se fizéssemos isso com um iterador, não obteríamos nenhum elemento na segunda vez em que fizemos o loop:

numbers = iter(range(3))
tuple(numbers)
# R:(0, 1, 2)
tuple(numbers)
#R:()

	# Ao contrário dos objetos zip, enumerate ou generator, os objetos range não são 6-iteradores.

	#-- ENTÃO O QUE É O RANGE? --##

	# O objeto range é "lazy" em certo sentido, porque não gera todos os números que "contém" quando o criamos. Em vez disso, ele nos fornece esses números conforme precisamos deles ao fazer 		um loop sobre ele.
    #
	# Aqui está um objeto range e um generator (que é um tipo de iterador):

numbers = range(1_000_000)
square = (n**2 for n in numbers)