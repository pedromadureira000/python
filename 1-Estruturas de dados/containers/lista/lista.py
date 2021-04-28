# É uma sequência ou coleção ordenada de valores que podem ser de diferentes tipos de objeto. Uma lista em uma outra
# lista é dita aninhada (nested) e a lista mais interna é chamada frequentemente de sublista (sublist). Finalmente, existe
# uma lista especial que não contém elemento algum. Ela é chamada de lista vazia e é denotada por [].

# A lista do python é semelhante a uma lista dinamica em  outras linguagens.



    #É possivel concatenar e multiplicar listas: lista + [0,1] ; lista*10
lista_mista = ["ola", 2.0] + 2*[5,3] + [[10, 20]] #define uma lista com elementos

    #criar lista
lista = list(range(10)) #retorna uma lista de 0 a 9
listaCharc = list("oi eu sou o pedro") #transforma em lista de caracteres

    #adicionar e remover itens
print(lista.append(4))  #adiciona valor no final da lista
print(lista.remove(4))  #remove remove um valor (da erro se nao houver o valor na lista)
print(lista.pop()) #remove um elemento da lista (padrao -1) (retorna o valor deletado)
print(lista.extend([1,2,4])) #adiciona objetos de uma lista a uma lista
print(lista.insert(0,"oi")) #insere no indice (0) o elemento ("oi"). Empura os elementos da e nao subistitui o elemento.

    #copiar e deletar lista
print(lista.copy())  #copia a lista" (retorna uma copia da lista)
print(lista.clear())  #limpa a lista

    #Ordenar lista
print(lista.reverse()) #reverte os elementos da lista
print(lista.sort())  #Ordena os elementos da lista em ordem crescente.

    #tamanho da lista
print(len(lista))  #retorna o tamanho da lista

#--------------------/index and slicing/-------------------------

lista_mista = ["ola", 2.0, 5*2, [10, 20]]  #define uma lista com elementos
lista = [1,2,3]
print(lista_mista[3][1]) #retorna o valor do indice 1 no objeto de indice 3
print(lista[:3]) #retorna tudo ate o indice 3(exclusivo)
print(lista[1:]) #retorna do indice 1 ate o final
print(lista[:]) #pega tudo (copia superficial(shallow copy) da lista)
print(lista[:-1]) #pega tudo menos a ultima letra
print(lista[::2]) #pega tudo de dois em dois
print(lista[::-1]) #pega tudo ao contrário

