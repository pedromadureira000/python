# https://docs.python.org/3/library/typing.html

from typing import List, Union, Tuple, Dict, NewType, Callable, Sequence, \
    Iterable

# Primitivos
numero: int = 10
flutuante: float = 10.5
booleano: bool = False
string: str = 'Luiz Otávio'

# Sequências
lista: List[int] = [1, 2, 3]
# lista: list = [1, 2, 3]
lista_str_int: List[Union[int, str]] = [1, 2, 3, 'Luiz']  # lista de varios tipos
tupla: Tuple[int, int, int, str] = (1, 2, 3, 'Luiz')

# Dicionários e conjuntos: Dict[key, value]

# Meu tipo
MeuDict = Dict[str, Union[str, int, List[int]]]  # Alias de tipo
# pessoa: Dict[str, Any]. O any nao é muito.
pessoa: Dict[str, Union[str, int]] = {
    'nome': 'Luiz Otávio', 'sobrenome': 'Miranda', 'idade': 30}
pessoa2: MeuDict = {'nome': 'Luiz Otávio',
                    'sobrenome': 'Miranda', 'idade': 30, 'l': [1, 2]}

# Meu outro tipo
UserId = NewType('UserId', int)
user_id = UserId(325456789)


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    # recebe um Callable(que recebe uma dois int como argumentos, e retorna um inteiro)
    # e retorna um Callable.
    return funcao


def soma(x: int, y: int) -> int:
    return x + y


print(retorna_funcao(soma)(10, 20))


class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')


def iterar(sequencia: Sequence[int]):  # quando vc vai receber qualquer sequencia
    return [x for x in sequencia]


def iterar2(sequencia: Iterable[int]):
    return [x for x in sequencia]


print(iterar([1, 2, 3]))
print(iterar((1, 2, 3)))
print(iterar2([1, 2, 3]))
print(iterar2((1, 2, 3)))