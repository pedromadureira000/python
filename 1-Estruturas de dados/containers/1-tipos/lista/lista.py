# É uma sequência ou coleção ordenada de valores que podem ser de diferentes tipos de
# objeto. Uma lista em uma outra lista é dita aninhada (nested) e a lista mais interna é chamada frequentemente de sublista
# (sublist). Finalmente, existe uma lista especial que não contém elemento algum. Ela é chamada de lista vazia e é denotada por [].

# considerado uma lista dinamica em  outras linguagens. É possivel concatenar listas: lista + [0,1] ; lista*10 (gera uma
# nova lista com os elementos repetidos

lista_mista = ["ola", 2.0, 5*2, [10, 20]]  #define uma lista com elementos
lista = [1,2,3]
uma_lista = list(range(10))
print(len(uma_lista))  #retorna o tamanho da lista
lista.append(4)
lista.remove(5) #remove remove um valor ou seja o objeto int 5
popped=lista.pop() #padrao é -1, portanto sempre remove  o ultimo elemento da lista
lista.reverse()# reverte os elementos da lista
lista.sort()#Ordena os elementos da lista em ordem crescente. Retorna ""none""
print(lista_mista[3][1]) #retorna o valor do indice 1 no objeto de indice 3
print(lista.extend([1,2,4])) #adiciona objetos de uma lista a uma lista
print(lista[:3]) #retorna tudo ate o indice 3( sem contar com ele)
print(lista[1:]) #retorna do indice 1 ate o final
print(lista[:]) #pega tudo
print(lista[:-1]) #pega tudo menos a ultima letra
print(lista[::2]) #pega tudo de dois em dois
print(lista[::-1]) #pega tudo ao contrário
print( lista + ["new item"]) #retorna a lista ""lista"" com o elementos adicionado
print(list(range(10))) #retorna uma lista de 0 a 9
lista.insert(0,1) #insere no indice (0) o elemento (1)
listaCharc= list("oi eu sou o pedro") #transforma em lista de caracteres
print("".join(listaCharc)) #pega uma lista de caracteres(se for uma string vai pegar um #caractere por fez da msm forma),
#e adiciona um por um ao elementro entre """", #retornando uma string no final
lista.clear()  #limpa a lista
lista2=lista.copy()  #copia a lista"


