class Objeto:
    def __init__(self,par):
        self.par = par

class Teste:
    def __init__(self,parobjeto):
        self.parobjeto = parobjeto

insobjeto = Objeto(1)
insteste = Teste(insobjeto)

print(id(insteste.parobjeto) , id(insobjeto.par))
insteste.parobjeto = 2
print(insobjeto.par)
assert insobjeto.par == insteste.parobjeto


#por que em test_envio_para_base_de_usuarios.py:32 "assert len(usuarios) == enviador.enviar.call_count" nao deveira ser
#enviador_de_spam.enviar.call_count,como que o parametro esta fazendo referencia ao outo ?
from unittest.mock import Mock
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'pedro@solucoesweb.com',
        'assunto',
        'corpo do email'
    )
    assert len(usuarios) == enviador.enviar.call_count


class EnviadorDeSpam:
    def __init__(self, sessao, enviador):
        self.sessao = sessao
        self.enviador = enviador

    def enviar_emails(self, remetente, assunto, corpo):
        for usuario in self.sessao.listar():
            self.enviador.enviar(
                remetente,
                usuario.email,
                assunto,
                corpo
            )