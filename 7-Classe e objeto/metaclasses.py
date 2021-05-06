"""Metaclasses são classes que criam outras classes. Servem para criar
 restrições para criação de metodos e atributos de classes filhas, criar design patters tbm."""
class Meta(type):  #type é uma metaclasse, que pode ser usada pra criar classes
    # mcs(a metaclasse), name(nome da classe q esta sendo criada), namespace (tod0 atributo e metodo da classe)
    # base: é as classes pai das classes q estao sendo criadas.
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)
        if 'b_fala' not in namespace:
            print(f'Oi, você precisa criar o método b_fala em {name}')
        else:
            if not callable(namespace['b_fala']):
                print(f"o atributo b_fala precisa ser um metodo, em {name}")
        if 'attr_classe' in namespace:  #isso impede a sobrescrita do atributo, por herdeiros da classse "A"
            print(f'{name} tentou sobrescrever o atributo.')
            del namespace['attr_classe']
        return type.__new__(mcs, name, bases, namespace)

#toda classe/objeto que herdar de A, vao seguir as regras de __new__ na metaclasse 'Meta'.
class A(metaclass=Meta):
    def fala(self):
        self.b_fala()
    attr_classe = 'valor A'

class B(A):
    def b_fala(self):
        print("oi")
    attr_classe = 'valor B'

class C(B):
    def b_fala(self):   #as classes herdadas de A, precisam criar o metodo b_fala.
        print("oi")
    attr_classe = 'valor C'   #nem B, nem C, conseguiram sobrescrever o attr de A.
c = C()
print(c.attr_classe)

#---/criando classe com type
A = type(
    'A', #nome da classe
    (C,),  #tupla de quem ela herda
    {'attr':'Olá Mundo!'}  #atributos
)
a = A()
print(type(a))

