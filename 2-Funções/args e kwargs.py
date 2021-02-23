#                                                      *args

#por conveção chama-se de args. Recebe um numero arbitrario de parametros posicionais (nao nomeados/justapostos) e retorna os empacota em uma tupla
def soma(*args):
    print(args) #R:(1, 'dois', True)
    print(type(args)) #R:<class 'tuple'>
soma(1,"dois",True)

#______________________________________________________________________________________________________
#                                                    **kwargs

#por convenção chama-se kwargs (key world arguments). Recebe um numero arbitrario de parametros nomeados. E retorna um dicionario
def f(**kwargs):
    print(kwargs) #R:{}
    print(type(kwargs)) #R:<class 'dict'>

f()
f(nome = "Pedro", idade = 22, Sobrenome = "Henrique")

#______________________________________________________________________________________________________

#                                               *args e **kwargs

#recebendo parametros nomeados e posicionais. Os nomes inseridos no args vao pra tupla e os no kwargs vao  pro dicionario
def var(*args, **kwargs):
    print(args) #R:(1, 2)
    print(kwargs) #R:{'nome': 'Joao', 'sobrenome': 'sobrenome'}
var()
var(1,2,nome= 'Joao',sobrenome='sobrenome')

#______________________________________________________________________________________________________

#                                              z-desenpacotamento-z de *args e **kwargs
args = (2,4,10)
kwargs = {'nome':"pedro",'sobrenome':"henrique"}
var(args,kwargs) # vai ser considerado dois parametros posicionais e vao cair em *args

#z-desenpacotamento-z: use o * para tuplas(converte em parametros posicionais), e ** para dicionarios(converte em parametros nomeados)
var(*args, **kwargs)  #R:(2, 4, 10)  e  {'nome': 'pedro', 'sobrenome': 'henrique'}






