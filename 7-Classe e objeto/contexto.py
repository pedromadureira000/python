#------------------------/com classe (forma manual)/---------------------------

class Arquivo:
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):  #no with Arquivo.., ira chamar o __enter__, para retornar o arquivo
        print('retornando arquivo')
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('fechando arquivo')
        self.arquivo.close()
        # Vc precisaria tratar as exeções, para dps retornar true.
        return True

with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')

#------------------------/com @contextmaneger ---------------------------

from contextlib import contextmanager


@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')