#a função sempre procura primeiro no escopo local e depois no global. Mas se dentro do escopo de uma função
# vc tentar atribuir um valor a uma variavel global, o python vai criar uma variavel local com esse nome, e nao vai
# mais utilizar a variavel global dentro do escopo em que vc esta.

#-----------------/codigo correto/--------------------------
string = "carrro"
strordenada = sorted(string)
caracter_anterior = strordenada[0]
counter = 1

def contador(strordenada):
    global caracter_anterior, counter  #OBS1

    print(caracter_anterior)
    for caracter in strordenada[1:]:
        if caracter == caracter_anterior:
            counter += 1

        else:
            print(counter,caracter_anterior)
            caracter_anterior = caracter  #OBS2
            counter = 1
contador(strordenada)

#OBS1: importa para o corpo da função as variaveis globais, de modo que o interpretador não procure por ela localmente.
#OBS2: modifica a variavel global, ao invez de criar uma local (gerando erro na linha 14)

#-----------------/codigo errado/--------------------------
string = "carrro"
strordenada = sorted(string)
caracter_anterior = strordenada[0]
counter = 1

def contador(strordenada):
    print(caracter_anterior)
    for caracter in strordenada[1:]:
        if caracter == caracter_anterior:
            counter += 1
        else:
            print(counter,caracter_anterior)
            caracter_anterior = caracter   #essa operação causa erro, pois faz com q esse namespace seja criado localmente
                                           #e o print não encontra mais a variavel global
            counter = 1
contador(strordenada)