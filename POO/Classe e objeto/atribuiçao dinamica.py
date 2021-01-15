class Pessoa:
    def __init__(self, *filhos, nome=None, idade=0):
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f"ola {id(self)}"

if __name__ == '__main__':
    pedro = Pessoa(nome="Pedro")
    henrique = Pessoa(pedro, nome="Henrique")
    henrique.sobrenome = "Pedro"                     #vc pode adicionar novos atributos em um objeto
    print(henrique.sobrenome)
    print(henrique.__dict__)
    print(pedro.__dict__)
    del henrique.sobrenome      #vc pode deletar atributos dinamicamente, msm sendo um atributo definido em __init__
    print(henrique.__dict__)    #isso não é uma boa pratica
