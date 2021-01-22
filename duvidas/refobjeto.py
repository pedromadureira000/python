# um objeto criado no corpo de uma função e enviado como parametro para outra função,
# quando modificado no corpo da priemira função, tbm modifica na segunda função? (o objeto
# passado como argumento passa a existir duas vezes no corpo das duas funções? ou apenas no
# corpo da primeira, sendo apenas refenciado na segunda?)

class Testeprintanum:
    def __init__(self):
        self.num = None

    def mudanum(self,num):
        self.num = num

    def printanum(self):
        print(self.num)
        
class Objetoteste:
    def __init__(self, a=None):
        self.a = a

            #teste com objeto
class Teste:
    def testerefobjeto(self):
        objetoteste = Objetoteste()
        numeroteste = Testeprintanum()
        numeroteste.printanum()
        numeroteste.mudanum(objetoteste.a)
        objetoteste.a = "wtf"
        numeroteste.printanum()
aa = Teste()
aa.testerefobjeto()

        #teste com lista

class Teste:
    def testerefobjeto(self):
        objetoteste = [Objetoteste(),]
        numeroteste = Testeprintanum()
        numeroteste.printanum()
        numeroteste.mudanum(objetoteste)
        objetoteste = "wtf"
        numeroteste.printanum()
aa = Teste()
aa.testerefobjeto()

