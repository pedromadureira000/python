import sys
import time

lista = [0, 1, 2, 3, 4]


# ------------------------------------/4-iteração sem gerador/----------------------------------------------#

# ----/Aqui será gerado a lista e so depois vai iterar
def gera():
    r = []
    for n in range(10):
        r.append(n)
        time.sleep(0.1)
    return r


g = gera()  # gerando a lista
for v in g:  # iterando sobre a lista
    print(v)


# ------------------------------------------4-iteração com gerador---------------------------------------------#
# ---/aqui vai iterando ao mesmo tempo q cria a lista.
def gera():
    for n in range(10):
        yield n
        time.sleep(0.1)


g = gera()  # o g é agora um gerador, que é um iterador
print(g)  # retorna: <generator object gera at 0x7f4bf31a4af0>
for v in g:  # como g é um gerador, ele gera os valores enquanto é feita a 4-iteração
    print(v)

print(hasattr(g, '__iter__'))  # mostra que o objeto possui o atributo de um iterador
print(hasattr(g, '__next__'))


# para chamar o proximo numero: print(next(g))   , vc nao pode fazer isso agr pois vai dar erro "StopIteration", por
# estar esgotado


def gera():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


g = gera()
print(next(g))
print(next(g))
print(next(g))

# -------------------------------------/criando gerador com compreenção de listas/-------------------------------------
lista = [x for x in range(10)]  # exemplo de criação de lista
gerador = (x for x in range(10))  # criação de gerador
print(type(lista))
print(type(gerador))
print(sys.getsizeof(lista))

# tamanho da lista é 9024 bytes, e cresce conforme o tamanho da lista
for n in gerador:
    print(n)
    print(sys.getsizeof(gerador))
# o tamanho do gerador é sempre 88 bytes,e so vai ti entregar o valor quando vc pedir.


# ----------------------/exemplo de q a quando há a suspenção da funções do gerador, se retomada/----------------------
# sua execução, continua no ultimo ponto de geração de valor.
gerador = (x for x in range(10))
for n in gerador:
    if n > 5:
        break
    print(n)
for n in gerador:
    print(n)
# retorno:
# 1
# 2
# 3
# 4
# 5
# 7
# 8
# 9
