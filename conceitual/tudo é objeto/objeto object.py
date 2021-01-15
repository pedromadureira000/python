"""tudos osbjetos do python herdam o objeto object
é uma intervace padrão para todos objetos python, inclusive os built-in. Ou seja os objetos que vc cria não sao nada diferentes dos
objetos do proprio python. Desse forma o modelo de dados é seguido dentro da propria linguagem, existem outras linguagens que nao sao
assim, e nao seguem o 'protocolo de meta objeto'(java, C#),e nelas existem metodos built-in que fazem coisas que vc n consegue fazer.
No python vc consegue interagir com o python da mesma forma que os tipos nativos da linguagem, com seus objetos.


"""

class vazio:
    pass
print(set(dir(object)) - set(dir(vazio)))  #R retorna um conjunto varzio, pois todas definições de "object" são iquais as de "vazio"


    #metodos herdados de object

#__init__  é o metodo inicializador da classe, como a classe vai ser inicializada
"self ? em oposição a cls da classe"
#__new__   é o metodo construtor da classe, como a classe vai ser construida,
"usa cls, q é uma instancia da classe"

#__repr__  é a representação da classe

#__str__ é a string da classe

#__doc__ é a documentação da classe


#--------------------------------

#decoradores de classe: static method, class method, todos eles usam cls, eles nao compartilham da instancia e sim do
#esqueleto da classe

#https://www.youtube.com/watch?v=syctPjStwQU&t=1030s
#27 min
