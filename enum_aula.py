"""Serve para quando vc quer uma lista de valores possiveis que vao ser usados para validar uma entrada de uma função/metodo"""
from enum import Enum, auto


class Directions(Enum):
    right = auto()
    left = auto()  # o auto atribui um valor numerico para cada nome.
    up = auto()
    down = auto()


def move(direction):
    if not isinstance(direction, Directions):  # verifica se o movimento passado esta na lista de movimentos permitidos
        raise ValueError('Cannot move in this direction')

    return f'Moving {direction.name}'


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))

    print()

    for direction in Directions:
        print(direction, direction.value, direction.name)
