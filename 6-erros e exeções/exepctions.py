class MinhaException(Exception):
    pass

def exemploexecao():
    try:
        print("O codigo no corpo de 'try', vai tentar rodar os comandos, e caso gere erro, irá rodar o 'except'. ")
    except MinhaException:
        print("except serve para tratar uma exeção, caso ocorra uma em 'try'")
    else:
        print("else é executado caso nao ocorra nenhuma exeção em 'try'.")

exemploexecao()
