# https://rszalski.github.io/magicmethods/

class A:
    def __new__(cls, *args, **kwargs):  #cria uma instancia de object
        print('Método new foi chamado')
## SINGLETON (so pode existir uma instancia dessa classe)
        if not hasattr(cls, '_jaexiste'):
            cls._jaexiste = super().__new__(cls)

        return cls._jaexiste

    def __call__(self, *args, **kwargs):  #faz o objeto da classe se comportar como uma função
        return f'Argumentos enviados: {args} {kwargs}'

    def __len__(self):   #se vc tiver um objeto com varios objetos dentro, pode contar e retornar no len
        return 55

    def __init__(self, nome=None):
        print('INIT')

    def __str__(self):  #serve para printar o objeto
        return f'O que quero exibir quando essa classe se transformar em uma str'
#sem isso o print retorna: <__main__.A object at 0x7f484fd6a3d0>
# ( __main__, por q o objeto esta sendo executado no msm modulo.)

    def __del__(self):    #vai ser executado quando o garbage collector deletar esse objeto(quando n estiver + sendo usado)
        print('Objeto coletado.')
#nem sempre esse metodo é chamado, por isso n pode confiar nele pra fazer algo muito importante. A docuemntação do python
#nao recomenda usar esse metodo.
    def __setattr__(self, key, value):   #adiciona atributos que vc tentou criar para o objeto( a.key = "value")
        self.__dict__[key] = f'{value} adicionei isso no seu valor'


a = A('luiz otávio')
print(a)