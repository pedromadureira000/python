class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade = 0):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_statico():
        return 42

    @classmethod
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    def metodo(self):
        #metodo_da_classe_pai = Pessoa.cumprimentar(self)  # Poderia fazer assim, mas não seria tao bom
        metodo_da_classe_pai = super().cumprimentar()
        return f'{metodo_da_classe_pai}. Coloque aqui o codigo adicional'

if __name__ == '__main__':
    pedro = Homem(nome="Pedro")
    henrique = Homem(nome="Henrique")
    print(pedro.metodo())
