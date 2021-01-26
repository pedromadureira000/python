# 	test_fase.py
# classe PassaroFake, o que é esse "super().__ini__ ?

class ClassePai:
    def __init__(self,x, y,z ):
        self.z = z
        self.y = y
        self.x = x
    def priter(self):
        print(self.x, self.y,self.z)

class ClasseFilho(ClassePai):
    def __init__(self, x, y,z):
        super().__init__(x, y, z)   #o que isso faz ?
    def priter(self):
        print(self.x, self.y, self.z)

filho = ClasseFilho(True, True, False)
filho.priter()
