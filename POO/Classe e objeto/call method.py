class Pessoa:
    def cumprimentar(self):
        return f"ola {id(self)}"

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))    #vc pode chamar o metodo apartir da classe, passando um objeto
                                     # dessa classe como parametro self

    print(p.cumprimentar())          #quando vc chama o metodo apartir do objeto vc nao precisa passar o
                                     # objeto como parametro(self), ele sera passado implicitamente
    print(id(p))
