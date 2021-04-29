    # count()    (indice do elemento)
l = ["a","b","c"]
l.count(2)  #retorno: 1


    # type()
print(type(1)) #retorno: 'int'


# zip()
x = [1, 2, 3]
y = [2, 3, 4]
print(list(zip(x, y)))  # retorno: [(1, 2), (2, 3), (3, 4)]

# enumerate()
lst = ['a', 'b', 'c']
for number, item in enumerate(lst):
    print(number)
    print(item)

for count, item in enumerate(lst):
    if count >= 2:
        break
    else:
        print(item)

        # all() e any()
lst = [True, True, False, True]
print(all(lst))  # retorna False
print(any(lst))  # retorna True

# ----------------------/modulos importados / ---------------------------

# nametuple()
from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='lab', name='sammy')
frank = Dog(age=2, breed='Shepard', name='Frankie')
print(sam)
print(sam.age)
print(sam.breed)
print(sam[2])

# ordereddict()
# OrderedDict
from collections import OrderedDict

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'
d2 = OrderedDict()
d2['b'] = 'B'
d2['a'] = 'A'
print(d1 == d2)  # False
# ele leva em conta a ordem de lançamento de valores no dicionario

# counter()
# couter
from collections import Counter

l = [1, 2, 3, 44, 5, 6, 6, 5, 2, 1, 1, 23, 2]
coun = Counter(l)
print(coun)
# retorna: Counter({1: 3, 2: 3, 5: 2, 6: 2, 3: 1, 44: 1, 23: 1})
# a chave é o elemento e o valor a contagem do elemento.

# getcwd()
from os import getcwd

where_i_am = getcwd()
# --------------------------------------

# randint()
from random import randint

print(randint(1, 60))
# --------------------------------------


