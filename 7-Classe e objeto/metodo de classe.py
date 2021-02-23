class Pessoa:
    olhos = 2
    def cumprimentar(self):          #metodo de instancia, acrescenta self automaticamente
        return f"ola {id(self)}"
    @staticmethod
    def metodo_statico():           #metodo statico: funciona como uma função atrelada ao objeto Pessoa
        return 42
    @classmethod
    def metodo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())
    print(id(p))
    #vc pode chamar o metodo apartir da classe, passando um objeto dessa classe como parametro self
    # quando vc chama o metodo apartir do objeto vc nao precisa passar o objeto como parametro(self)
    #ele sera passado implicitamente
    print(p.metodo_statico(), Pessoa.metodo_statico())
    print(p.metodo_de_classe(), Pessoa.metodo_de_classe())
