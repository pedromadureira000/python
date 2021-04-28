#a declaração de tipos no python so tem valor documental. Ao executar o codigo nao vai fazer nenhuma diferença

def soma(x: float = 1, y: float = 2,) -> float:
    return x+y

    #notação para dicionario e lista
from typing import Dict, List

def exemple(dicio: Dict[str, int] = {}, lista: List[int] = []) -> tuple:
    return dicio, lista

