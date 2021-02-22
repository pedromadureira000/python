# try e except: o codigo q pode causar uma exceção é colocado no bloco try, e o tratamento da exceção é implementado no bloco except.
def string(n="1"):
    try:
        a = "1" + n
    except:
        print("parâmetro invalido, uma exceção ocorreu")
        raise Exception("Mês Inválido")
        # força o erro e mostra uma mensagem. sem raise o programa continua
    finally:
        print("finally sempre será executado")

string(1)