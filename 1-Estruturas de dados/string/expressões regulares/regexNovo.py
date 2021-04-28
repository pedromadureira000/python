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
#OBS: se houver apenas grupos com ?: eles seram retornados. Se houver grupos com e sem ?:, sera retornado apenas os sem ?:
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


#--------------------/definir começo e fim. E negação de conjuntos/----------------------------------------------

# ^ = começa com         (bom pra validar campos onde um usuario envia um dado especifico)
# $ = termina com
# [^a-z] = negação (traz qualquer coisa que não seja "a-z")

cpf = 'a 147.852.963-12 a' #nao valida
cpf = '147.852.963-12 a' #nao valida
cpf = '147.852.963-12' #valida

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
print(re.findall(r'[^a-z0-9.-]+', cpf)) #negei tudo e nao trouxe nada.

#--------------------/seguências especiais (Shorthand) /----------------------------------------------
texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.
Foi um ano excelente na vida de joão. Teve_ALGO 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''
# \w -> [a-zA-Z0-9À-ú_]
print(re.findall(r'\w+', texto))

# \w -> [a-zA-Z0-9_] -> re.A
print(re.findall(r'\w+', texto, flags=re.A))

# \W -> [^a-zA-Z0-9À-ú_]    #com "W" maiusculo, vc tem a a negação do "\w"
print(re.findall(r'\W+', texto))

# \W -> [^a-zA-Z0-9_] -> re.A
print(re.findall(r'\W+', texto, flags=re.A))

# \d -> [0-9]       #qualquer número


# \D -> [^0-9]

# \s -> [ \r\n\f\n\t]   #qualquer espaço em branco
print(re.findall(r'\s+', texto, flags=re.I))

# \S -> [^ \r\n\f\n\t]   #encontra tudo que não for espaços
print(re.findall(r'\S+', texto, flags=re.I))

# \b -> borda            #encontra a borda ( uma string vazia)
# serve pra encontrar palavras que começam ou terminam de um jeito expecifico
print(re.findall(r'\be\w+', texto, flags=re.I))  #palavras que começam com e
print(re.findall(r'\w+e\b', texto, flags=re.I)) #palavras que terminam com e
print(re.findall(r'\b\w{4}\b', texto, flags=re.I)) #palavras que com 4 letras (sem a borda ele pegaria as 4 primeiras letras
                                                   #de palavras com mais de 4 letras.)

# \B -> não borda
print(re.findall(r'Flores\B', texto, flags=re.I)) #procura por "Flores", mas sem borda no final


#-----------------------------------------/flags/----------------------------------------------

#re.A  = ASCII   (sem acentos)

#re.I = IGNORECASE

#re.M = Multiline      ^ e $ passam a representar o começo e o fim da linha, ou invez do começo e o fim da string.

#re.X VERBOSE   (PERMITE ESCREVER COMENTARIOS NA EXPRESSÃO E USAR TRIPPLE COTES.

texto = '''
131.768.460-53  asdf
055.123.060-50   df
955.123.060-90
'''
print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto, flags=re.M))  #procura o padrão, por linha, ao invez de usar a regra no texto tod0.

#re.S = Dotall
# é bom quando vc quer econtrar um padrão com começo e fim predefinidos, vc vai usar um ".*", e pode ter quebra de linha no meio.)
# O ".*" não reconhece quebra de linha, então é necessário usar a flag re.S

texto2 = '''O João gosta de folia 
E adora ser amado'''
print(re.findall(r'^o.*o$', texto2, flags=re.I))  # sem re.S
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))  # com re.S


#-----------------------------------------/Lookahead e lookbehind/----------------------------------------------
#Lookhead e Loockbihind não retornam nada, apenas checam. O que retorna é a expressão regular

# Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))   #termine com "active

# Negative lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))  #nao termine com "active"

# Positive lookahead
pprint(re.findall(r'(?=.*[^in]active).+', texto))
#quero a string a linha q termina com "active", sem "in" antes de "active", e com qualquer coisa antes de active

# Positive lookbehind
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto)) #esse nao precisa do "\w" antes
#procura por "online" antes de (\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+')

# Negative lookbehind
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto)) #precisa do "\w" antes
#procura por strings que não tenham "online" antraz de (\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+')

# Positive lookbehind
pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

# Negative lookbehind
pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))

#-----------------------------------------/EX: CPF e IP  /----------------------------------------------

# 0.0.0.0 255.255.255.255
# 025.258.963-10 02525896310

# Teste essa expressão
# em https://regex101.com/r/lWVPOr/1
cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', flags=0)
# print(cpf_reg_exp.search(cpf))

# Teste essa expressão
# em https://regex101.com/r/XDyL7q/1
ip_reg_exp = re.compile(
    r'^'  # Começa com
    r'(?:'
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.'
    r'){3}'  # Sequência de 3 digitos e um ponto repete 3x
    r'(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])'
    r'$',  # Termina com
    flags=0
)

for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'

    print(ip, ip_reg_exp.findall(ip))

    #em uma linha só

print(re.findall(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$', "235.236.237.238"))


#-----------------------------------------/EX: CPF Validado com Negativelookahead/----------------------------------------------
# https://regex101.com/r/0OM1oz/1/

#não captura seguencias de so numero, tipo: 000.000.000-00

import re
from pprint import pprint


regex = re.compile(
    r"^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})(\d{3}\.\d{3}\.\d{3}-\d{2})$",
    flags=re.MULTILINE
)

test_str = ("698.547.520-54\n"
            "060.235.190-16\n"
            "683.134.960-96\n"
            "899.344.730-62\n"
            "103.778.870-21\n"
            "721.478.580-30\n"
            "366.310.090-14\n"
            "794.289.350-26\n"
            "190.259.410-01\n"
            "000.000.000-01\n"
            "900.000.000-00\n\n"
            "000.000.000-00\n"
            "111.111.111-11\n"
            "222.222.222-22\n"
            "333.333.333-33\n"
            "444.444.444-44\n"
            "555.555.555-55\n"
            "666.666.666-66\n"
            "777.777.777-77\n"
            "888.888.888-88\n"
            "999.999.999-99\n\n"
            )

pprint(regex.findall(test_str))

#-----------------------------------------/EX: Telefone----------------------------------------------

import re

# https://regex101.com/r/DfXYXM/1/
regexp = re.compile(r'^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4}-\d{4})$', flags=re.M)
#(?:  ) (?:  ) (?:  )  Trez grupos com :? retornam tudo em uma string, ao invez de 3 retornos numa tupla
#((  ) (  ) (  ))   Um grupo com 3 grupos aninhados: retorna uma tupla com os 4 grupos, começando pelo grupo pai
texto = '''
(21) 9 8852-5214
(11)9955-1231
(11)            9955-1231
(35) 9 9975-4521
(31) 3851-2587
9 8571-5213
1234-5647
'''

for telefone in regexp.findall(texto):
    print(telefone)

#-----------------------------------------/EX: Senha----------------------------------------------
# https://regex101.com/r/W4kRV2/2/
# https://en.wikipedia.org/wiki/List_of_Unicode_characters
import re
senha_forte_regexp = re.compile(
    r'^'
    r'(?=.*[a-z])'
    r'(?=.*[A-Z])'
    r'(?=.*[0-9])'
    r'(?=.*[ -\/:-@[-`{-~])'
    r'.{12,}'
    r'$',
    flags=re.M
)

string = '''
VÁLIDAS
v2Ts7<o9T~}Y
j25TTbjJ:6{<
s`Mu6T;4M1!y
Li`hk6:3WX>3
d.D09}^dI2Vn
SEM MINÚSCULAS
I7^Y3RS^ 9]7
[P6W"83L5V{[
B7=;K8D6_}W5
1B_RT`93R%>1
EZU{7;2&D:64
SEM MINÚSCULAS E NÚMEROS
E}LV`C?X_G:{
AJH[@HD*V~=<
\A~AC{_V~MG 
W<-T}W:QAF'{
~YJ}|FILN>~)
SEM NÚMEROS CARACTERES E MINÚSCULAS
PBDZDPECUDNN
EJQWFWFFDEHY
XRCNLNRHYOZJ
TWIYPLWUDMNN
JMDTJSEPKVON
QUANTIDADE INVÁLIDA (6)
Iu4<1j
1x`P6g
@9t3Ry
qf9_6H
0o`9fO
'''

print(senha_forte_regexp.findall(string))


#-----------------------------------------/EX: Senha----------------------------------------------