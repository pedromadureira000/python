def ola(nome,sobrenome='Henrique',idade=18):
    print(f'olá {nome}{sobrenome} que tem {idade} de idade')
ola("Pedro","Da silva", 21) #os parametros são passados por justaposição

ola("Pedro",idade=22) #caso parametro seja passado sem ser nomeado, ele sera atribuido por justaposição
# caso parametro seja passado por nome do parametro, a posição do parametro deixa de importar