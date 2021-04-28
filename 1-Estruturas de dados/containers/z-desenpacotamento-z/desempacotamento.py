# desempacotamento pode ser feito a partir de tuplas, listas,
# se não tiver a mesma quantidade de parametros do que aqueles q existem vai dar erro.

tupla = ('renzo', 35)
nome, idade = tupla

lista = ['luiz', 'joao', 'maria', 1, 2, 3, 4, 5, 6, 7]
n1, n2, n3, *outros, penultimo, ultimo = lista  # usa asterisco para enviar um conjunto variavel de parametros para uma lista

    # desempacotamento para passar um argumento
def listar_itens(w, x, y, z):
    print(w, x, y, z)
lista = [12, 32, 43, 55]
listar_itens(*lista) #vai desenpacotar para enviar cada valor da tupla como parametro

    #desenpactomento de tupla com um laço for
tupla = ("sator", "arepo", "tenet", "opera", "rotas")
for des, en, paco, ta, mento in tupla:
    print(des, en, paco, ta, mento)

    #enumerate
string = 'adfa'
for indice, elemento in enumerate(string):
    print(indice, elemento)

    #desenpacotamento com *args

def my_sum(*args):
    print(args)  #*args recebe um numero variavel de parametros que são empacotados em uma tupla
    print(type(args)) #type tuple
    print(sum(args)) #função soma
my_sum(1,2,3,4)