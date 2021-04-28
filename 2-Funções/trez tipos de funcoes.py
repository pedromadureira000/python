def func_nomeada ():   #type(func_nomeada)  R:  <class 'function'>
    return "oi"

lambda : "oi" #type(lambda : "oi")  R:  <class 'function'>

class ClassFunction:    #type(ClassFunction) R: <class 'type'>
    def __call__(self): #type(ClassFunction() R: <class '__main__.ClassFunction'>     (se vc dar uma instancia do ClassFunction)
        return "oi"     #type(ClassFunction.__call___)  R: <class 'method'>  isso é um metodo e nao uma função

print(ClassFunction()())  #R: chama o metodo da classe diretamente pela classe
minha_classe_funcao = ClassFunction()
print(minha_classe_funcao())  #R chama o metodo da instancia da classe
