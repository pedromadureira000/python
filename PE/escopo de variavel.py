string = "carrro"
strordenada = sorted(string)
caracter_anterior = strordenada[0]
counter = 1
            #sem função

# for caracter in strordenada[1:]:
#     if caracter == caracter_anterior:
#         counter += 1
#
#     else:
#         print(counter,caracter_anterior)
#         caracter_anterior = caracter
#         counter = 1

            #com função

def contador(strordenada):
    print(caracter_anterior)
    for caracter in strordenada[1:]:
        if caracter == caracter_anterior:  # porque caractere_anterior náo é encontrado
            counter += 1

        else:
            print(counter,caracter_anterior)
            caracter_anterior = caracter
            counter = 1
contador(strordenada)



#a função sempre procura primeiro no escopo local e depois no global. Mas se dentro do escopo de uma função
# vc tentar atribuir um valor a uma variavel global, o python vai criar uma variavel local com esse nome, e nao vai
# mais utilizar a variavel global dentro do escopo em que vc esta.