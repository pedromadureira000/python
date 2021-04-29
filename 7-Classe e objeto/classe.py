# nomes de classes sempre devem comerçar com letra maiuscula
# classes podem ter atributos e metodos. E tem alguns metodos especiais como:
# __init__(selv, breed)  para iniciar atributos
# __str__(self):  é o metodo print(objeto)
# __len__(self): é o metodo que traz uma contagem de qtd
# __del__(self): é o metodo para o comando se deleta o objeto com del

#------------ATRIBUTOS-------------------------
class Dog():
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
sam = Dog(breed='Lab', name='Sam')  #instanciou a classe
frank = Dog(breed='Huskie',name='Frank')
print(type(sam)) #veja o tipo de objeto
#---------------METODOS----------------------
class Circle():
        pi=3.14
        def __init__(self, radius=1):
            self.radius = radius
        def area(self):
                return self.radius * self.radius * Circle.pi
        def setRadius(self, radius):
                self.radius=radius
        def getRadius(self):
                return self.radius
c = Circle(2)
print(c.radius)
print('o raio é ', c.getRadius())
print('a area é ', c.area())
#-------------METODOS ESPECIAIS-------------
class Book(object):
    def __init__(self, title, author, pages):
        print("a book is created")
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return "Title:%s, author:%s, pages:%s"%(self.title,self.author,self.pages)
    def __len__(self):
        return self.pages
    def __del__(self):
        print("a book was destroyed")
book = Book("Python Book","Pedro Madureira", 203)
print(book)
print(len(book))
del book