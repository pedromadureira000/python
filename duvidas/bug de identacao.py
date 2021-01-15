#------------ATRIBUTOS-------------------------
class Dog(object):
	def __init__(self, breed, name):
        self.breed = breed
        self.name = name
sam = Dog(breed='Lab', name='Sam')  #instanciou a classe
frank = Dog(breed='Huskie',name='Frank')
print(type(sam)) #veja o tipo de objeto
#---------------METODOS----------------------
class Circle(object):
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


