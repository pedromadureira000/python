class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)


class Homem(Pessoa):
    pass

pedro = Homem()
print(pedro.olhos)
# o interpretador procura olhos nos atributos do objeto, depois no da classe pai
# depois no da classe pai da classe anterior, até chegar em object.
#nesse caso, olhos sera encontrado na classe Pessoa.
print(pedro.__dict__)
#olhos é um atributo de classe da classe Pessoa e nao aparece em __dict__ da instancia pedro e
#da classe Homem.
print(Homem.__dict__)
print(Pessoa.__dict__)

        #SOBRESCRITA DE ATRIBUTO

class Mutante(Pessoa):
    olhos = 3

joao = Mutante()
print(joao.olhos)
print(joao.__dict__)
print(Mutante.__dict__)
#agora o retorno de olhos será 3, e nao vai procurar nas classes da qual essa foi herdada
