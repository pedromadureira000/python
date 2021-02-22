"essa string na primeira linha do codigo serve como documentação desse modulo. E sera retornada em help()"

def nada(x,y):
    """Na primeira linha vc diz o que a função faz. digete  '''|''' e de enter para carregar um template de
    documentação automaticamente

    :param x: number
    :param y: number
    :return: number
    """
    return x+y


    #se vc der um help(nomedomodulo) retorna:

#>>>
# Help on module ztestescompackage.imported in ztestescompackage:
# NAME
#     ztestescompackage.imported - essa string na primeira linha do codigo serve como documentação desse modulo. E sera retornada em help()
# FUNCTIONS
# nada(x, y)
#         Na primeira linha vc diz o que a função faz
#
#         :param x: number
#         :param y: number
#         :return: number
#
# FILE
#     /home/phsw/PycharmProjects/python/ztestescompackage/imported.py


"esse parametro da documentação se encontra em nomedomodulo.__doc__ "
"o parametro da documentação da função se encontra em nomedomodulo.nomedafunção.__doc__"

print(__doc__)
print(nada.__doc__)