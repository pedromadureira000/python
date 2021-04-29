class Pessoa:
    olhos = 2
    def cumprimentar(self):  #metodo de instancia: acessa atributos do objeto
        return f"ola {id(self)}"
    @staticmethod
    def metodo_statico(): #metodo statico: funciona como uma função atrelada ao objeto Pessoa (nao acessa atributos)
        return 42
    @classmethod         #metodo da classe: acessa atributos de classe
    def metodo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
if __name__ == '__main__':
    p = Pessoa()
    print(p.metodo_statico(), Pessoa.metodo_statico())
    print(p.metodo_de_classe())
    print(Pessoa.metodo_de_classe())
