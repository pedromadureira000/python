dicio = {"nome":"joão","apelido":"Ribeiro","altura":174} #define um dicionario
outrodicio = dict(nome = "paulo", apelido = "pedra", altura = 174) #define um dicionario
# print(dicio['apelido']) #retorna o valor do elemento 'apelido'
# print(dicio.get('nome')) #retorna o valor do elemento 'nome', porem caso nao encontre o valor, retorna null
# print(dicio.get('nomes', 'não definida')) #metodo get nao retorna erro caso nao ache a chave,vc tbm pode passar uma mensagem para caso não ache
dicio["apelido"] = "martins" #modifica o valor de "apelido" para "martins"

for key,valor in dicio.items():
    print(key,valor, "dicio.item()")  #printa as keys e valores,sendo o primeiro parametro a #key e o segundo o valor. Se vc passar apenas
    # uma variavel, o retorno será ('key','value')
print('nome'in dicio)


# for value in dicio.items():
#     print(value, "dicio.item()")  #printa as keys e valores,sendo o primeiro parametro a #key e o segundo o valor. Se vc passar apenas
#     # uma variavel, o retorno será ('key','value')