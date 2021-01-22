class MinhaException(Exception):
    pass

def exemploexecao():
    try:
        # exemploexecao()
        print("nenhum codigo que esteja no contexo da exeção vai ser executado")
    except MinhaException:
        print("except serve para tratar uma exeção")
    else:
        print("else é executado caso nao ocorra nenhuma exeção")

exemploexecao()
