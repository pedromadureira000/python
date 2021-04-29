# decoradores podem ser pensados como funções que modificam a funcionalidade de outra função.
#-----------/CRIANDO DECORADORES SEM @
def new_decorator(func):
    def wrap_func():
        print('code would be here, before executing the func')
        func()
        print("code here will execute after the func()")
    return wrap_func
def func_needs_decorator():
    print("this function is in need of a decorator")

func_needs_decorator = new_decorator(func_needs_decorator)
func_needs_decorator()  #É como se eu tivesse feito um "new_decorator(func_needs_decorator)()"

#---------/CRIANDO DECORADOR COM @
#O
@new_decorator
def func_needs_decorator():
    print("this function is in need of a decorator")
func_needs_decorator()