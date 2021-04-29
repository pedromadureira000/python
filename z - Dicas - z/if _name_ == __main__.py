#ATALHO:   Digite "main" e de um tab.

def main(x:float=1,y:float=2) -> float:
    return x+y
# isso pergunta se o codigo desse arquivo.py esta sendo executado dentro do arquivo principal ou como um modulo importado
#serve para evitar de executar os testes de um modulo que serve para ser importado.
if __name__ == '__main__': # __ é chamado de Dunder (double underline)
    main()

print(main())
print(__name__) #mostra (__main__) se a execução foi inicializada pelo proprio arquivo, ou __nomedomodulo__ se executado
#de uma importação feita por outro script python.