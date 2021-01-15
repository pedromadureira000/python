class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.filhos = list(filhos)


    def cumprimentar(self):
        return f"ola {id(self)}"



if __name__ == '__main__':
    pedro = Pessoa(nome="Pedro")
    henrique = Pessoa(pedro, nome="Henrique")
    print(henrique.filhos)
    for filhos in henrique.filhos:
        print(filhos.nome)

    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    print(pedro.cumprimentar)
