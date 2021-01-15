def contador() :
    string = input("digite uma string")
    resultado = {}
    for caracter in string:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado
print(contador())

#--------------------------/VERSÃO SEM VARIAVEL AUXILIAR/----------------------

def contador() :
    string = input("digite uma string")
    resultado = {}
    for caracter in string:
        resultado[caracter] = resultado.get(caracter, 0) + 1

    return resultado
print(contador())