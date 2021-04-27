import re
from pprint import pprint


text = 'this is a string with term1, but it does term1 not have the term1 other term .'
print(re.search(r'term1', text))
print(re.findall(r'term1', text))
print(re.sub(r'term1', 'ABC', text, count=1, ))
#count(padrão "zero" troca todas as vezes. Se por outro valor so ira subistituir essa qtd de vezes)

#----------------------/utilizando o compile/---------------------------------------
#compilar a expressão regular apenas uma vez.

regexp = re.compile(r'term1')
print(regexp.search(text))
print(regexp.findall(text))
print(regexp.sub("DEF", text))

#---------------------------/metacaracteres de regex/-----------------------------------
# Meta caracteres: . ^ $ * + ? { } [ ] \ | ( )
# | OU
# . Qualquer caractere (com exceção da quebra de linha)
# [] conjunto de caracteres ("range", que subistitui um caractere por outro que esteja no range)

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

print(re.findall(r'João|Maria|ad....s', texto))
print(re.findall(r'João|joão|Maria', texto))
print(re.findall(r'[Jj]oão|[Mm]aria', texto))
print(re.findall(r'[a-z]aria', texto))
print(re.findall(r'[a-zA-Z0-9_.]aria|[a-zA-Z0-9]oão', texto))  #o range vai ignorar o '.' e a '_'.
print(re.findall(r'jOãO|mAriA', texto, flags=re.I))

#--------------------/metacaracteres quantificadores/----------------------------------------------
# Meta caracteres: * + ? { }
# * = 0 ou n
# + = 1 ou n
# ? = 0 ou 1
# {n} = n quantidade de vezes
# {min, max} =

#OBS: o quantificador aplica a coisa q esta a sua esquerda, msm sendo um range [ ] ou grupo ( )
#()+ [a-zA-Z0-9]+

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.

Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm.
Jã"!
'''
# + = 1 ou n
print(re.findall(r'jo+ão+', texto, flags=re.I))
print(re.sub(r'jo+ão+', 'Pedro', texto, flags=re.I))
# * = 0 ou n
print(re.sub(r'jo*ão*', 'Luiz', texto, flags=re.I))  #pega até o "Jã"
# ? = 0 ou 1
print(re.sub(r'jo?ão', 'Carlos', texto, flags=re.I))  #vai procurar por "joão" ou "jão"

# {n} = n quantidade de vezes
# {min, max} =
# {10,} = 10 ou mais
# {,10} = zero à 10
# {10} = expecificamente 10

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm veeem veem vem"!
Jã
'''

print(re.findall(r'j[o]+ão+', texto, flags=re.I))
print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
print(re.findall(r've{3}m{1,2}', texto, flags=re.I))
# print(re.sub(r'jo{1,}ão{1,}', 'Felipe', texto, flags=re.I))

texto2 = 'João ama ser amado'
print(re.findall(r'ama[od]{0,2}', texto2, flags=re.I))
# com o quantificador {0,2} vc pega as combinações de 0 a 2 caracteres usando "o" e "d"


#--------------------/metacaracteres quantificadores/----------------------------------------------
# * 0 ou n
# + 1 ou n
# ? 0 ou 1


texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))
#quantificador greedy (guloso) (ambiguo) [procura o maximo de informação possivel]
#".*" continua checando apos o primeiro match e retorna tudo menos o ultimo "</div>", que é preciso pra fechar no final.

print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto)) #quantificador non greedy (nao guloso)
#vai parar no primeiro match e vai trazer todas combinações.
print(re.findall(r'<[dpiv]{1,3}>.+?<\/[dpiv]{1,3}>', texto)) #quantificador non greedy (nao guloso)


#--------------------/metacaracteres quantificadores/----------------------------------------------
# [] conjunto de caracteres ("range", que subistitui um caractere por outro que esteja no range)
#[a-z]+  (vai procurar combinações de letras minusculas)

# ( ) grupo de caracteres :  (encontra expecificamente o que esta dentro do grupo)
#(Luiz|Otávio) : (vai procurar combinações de "Luiz"(LuizLUiz) ou de "Otavio"(OtavioOtavio))

#OBS: quando vc utiliza grupos, é retornado apenas o que está dentro do grupo. Se vc por dois grupos, vai retornar o valor
#dos dois grupos em uma tupla.

# Os grupos sao contatos por chave aberta:
# () (grupo)    \1 (retrovisor)
# () ()  \1 \2
# (())()   \1 \2 \3

texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
print(re.findall(r'<([dpiv]{1,3})>.+?<\/\1>', texto))  #so retorna o que ta no grupo, por isso sai so um valor
print(re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto)) # retorna o que ta no grupo menor e no maior(que engloba tudo)

    #mostrar de forma mais bonita com pprint
tags = re.findall(r'(<([dpiv]{1,3})>.+?<\/\2>)', texto)
pprint(tags)

    #3 grupos, para seprar o conteudo dentro das tags

tags = re.findall(r'(<([dpiv]{1,3})>(.+?)<\/\2>)', texto)
pprint(tags)

    #pegando o apenas um dos valores com laço for e unpack

for tag in tags:
    um, dois, tres = tag
    print(tres)

    # criando um grupo que não sera salvo na memoria( e nao vai aparecer no resultado tbm)
#use "?:" no inicio do grupo
#isso é util para fazer um grupo so pra quantificar uma coisa(fazer alguma conta). Vai criar o grupo mas sem salva-lo, oq fará com que não
#exista o retrovisor referente ao grupo.
tags = re.findall(r'<([dpiv]{1,3})>(?:.+?)<\/\1>', texto)
pprint(tags)

    #exemplo CPF

cpf = 'a 147.852.963-12 a'

print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))

    #como os 3 digitos numericos precedidos por ponto se repetem duas vezes pode-se usar um grupo

print(re.findall(r'([0-9]{3}\.){2}[0-9]{3}-[0-9]{2}', cpf))
#como o grupo foi criado so pra usar o quantificador {2} e não ter q repetir o trecho, entao faça:
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

    #usando grupos nomeados
texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
tags = re.findall(r'<([dpiv]{1,3})>(.+?)<\/\1>', texto) #sem grupo nomeado
tags = re.findall(r'<(?P<tag>[dpiv]{1,3})>(.+?)<\/(?P=tag)>', texto)  #com grupo nomeado
pprint(tags)

    #colocando novos conteudos no texto, usando os grupos e retrovisores para montar

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))

# # for tag in tags:
# #     um, dois, tres = tag
# #     print(tres)