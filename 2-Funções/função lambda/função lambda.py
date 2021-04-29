# são chamadas funções anonimas(não tem nome, não é declarado como o def, e pode ser atribuido a uma variavel), ou
# expressões lambda. É caracterizado por ter no corpo uma expressão unica de retorno (semelhante ao return do def) ao invez
# de um bloco de declarações como as funções def. (lambda arg1,arg2: retorno_que_vc_quer)
# É bom pra quando vc precisa passar uma função como parametro para outra função, ou para algum metodo de alguma classe

quadrado = lambda num: num**2
print(quadrado(2))
#verificacoes
par = lambda num: num % 2 == 0
print(par(6))
#com indexação e slicing de strings
z = lambda s:s[0]
print(z("string"))
z1 = lambda s:s[::-1]
print(z1("string"))
#operacao com 2 parametros
ad= lambda x,y: x+y
print(ad(1,2))