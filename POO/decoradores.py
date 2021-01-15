# decoradores podem ser pensados como funções que modificam a funcionalidade de outra função.
#CRIANDO DECORADORES
def new_decorator(func):
    def wrap_func():
        print('code would be here, before executing the func')
        func()
        print("code here will execute after the func()")
    return wrap_func
def func_needs_decorator():
    print("this function is in need of a decorator")

#----abaixo é a criação de um decorador sem @
# func_needs_decorator = new_decorator(func_needs_decorator)
# func_needs_decorator()

    #CRIANDO DECORADOR COM @
@new_decorator
def func_needs_decorator():
    print("this function is in need of a decorator")
func_needs_decorator()