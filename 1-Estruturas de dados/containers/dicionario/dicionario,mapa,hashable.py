#--------------/DEFINIÇÃO DE UM DICIONARIO/-----------------

dicio = {"nome":"joão","apelido":"Ribeiro","altura":174}
outrodicio = dict(nome = "paulo", apelido = "pedra", altura = 174)

#--------------/INDEXAÇÃO DE UM DICIONARIO/------------------

print(dicio['apelido'])         #retorna o valor do elemento 'apelido'
print(dicio.get('nome'))        #retorna o valor do elemento 'nome', porem caso nao encontre o valor, retorna None
print(dicio.get('nomes', 'não definida'))    #vc tbm pode passar uma outro retorno para caso não ache
dicio["apelido"] = "martins"         #modifica o valor de "apelido" para "martins", ou cria um novo item


#-------------/TIPOS DE ITERAÇÃO COM DICIONARIOS/---------------------------

for key in dicio:                                      #--CHAVE
    print(key) #traz a chave
    print(dicio.get(key)) #traz o valor do item
    print((dicio[key])) #o msm q a linha acima


for value in dicio.values():                  #--VALOR
    print(value, 'dicio.values()')


for item in dicio.items():                    #--TUPLA COM CHAVE E VALOR
    print(item, "Itera com um argumento(chave) em dicio.item()")


for key,valor in dicio.items():               #--CHAVE E VALOR
    print(key,valor, "Itera com dois argumentos(chave e valor) em dicio.item()")

#-------------/OPERAÇÕES BOOLEANAS COM DICIONARIOS/---------------------------

print('nome'in dicio)

