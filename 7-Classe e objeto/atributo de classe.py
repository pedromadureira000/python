class Pessoa:
    olhos = 2  #esse é um atributo default ou atributo de classe. Não aloca na memoria para cada instancia da classe
    def __init__(self, *filhos, nome=None):
        self.nome = nome
        self.filhos = list(filhos)
pedro = Pessoa()
print(Pessoa.olhos)
print(pedro.olhos)        #o valor pode ser retornado pela classe ou objeto da classe.

print(id(Pessoa.olhos))
print(id(pedro.olhos))  #o atributo da classe é o mesmo para a classe e seu objeto instanciado.

print(pedro.__dict__)  #o dunderdict faz referencia apenas aos atributos de instancia
print(Pessoa.__dict__) #dunderdict na classe mostra os atributos de "object" e tambem mostra o atributo da classe

pedro.olhos = 1
#uma vez que eu mudei o valor do atributo de classe para um objeto, ele passa
#a fazer parte dos atributos de instancia dessa objeto.
print(pedro.__dict__)
print(id(pedro.olhos),id(Pessoa.olhos))
# O interpretador python busca primeiro nos atributos da instancia, depois nos da classe.
del pedro.olhos
#se vc deleta o atributo da instancia, sera retornado o de classe
print(pedro.olhos)

Pessoa.olhos = 3  #vc pode alterar o atributo da classe
print(pedro.olhos)   #nesse caso todos os objetos vao obter esse atributo, pois eles fazem referencia a ele

