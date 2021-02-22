# São padrões de correspondência de texto descritos com sintaxe formal. Muitas vezes você verá expressões regulares sendo referidas
# como 'regex' ou 'regexp'. As expressões regulares podem incluir uma variedade de regras, a busca de repetição, a correspondencia
# de texto entre outras. Muitos dos problemas de analize podem ser resolvidos com expressões regulares.
# O re.search() irá pegar o padrao, escanear o texto e retornar um objeto Match. Se nennhum padrão for encontrado, um None
# será retornado. Veja como é o objeto de correspondência: type(match) retorno: <class '_sre.SRE_Match'>
# Esse objeto match retornado pelo metodo search() é mais do que apenas um boolean ou None, ele contém informações sobre a busca,
# incluindo a string de entrada original, a expressão regular que foi usuada e a localização da corespondencia. Veja os metodos
# que podem ser usados no objeto de correspondencia.

#re.split(split_term,phrase)
#retorna uma lista com o termo removido e os termos na lista são uma versão dividida da sequencia de caracteres.

#re.findall('match',test phrase match is in middle')
#vc pode usar re.findall() para encontrar todas as instancias de um padrao em uma string.

import re
patterns = ['term1','term2']
text = 'this is a string with term1, but it does not have the other term.'
for pattern in patterns:
    print('searching for "%s" in:\n"%s"'%(pattern,text))
    #checa por correspondencia
    if re.search(pattern, text):
        print('\n')
        print('match was found. \n')
    else:
        print('\n')
        print('no match was found \n')
pattern = "term1"
match = re.search(pattern,text)
print(match)
print(match.start()) #mostra o indice de inicio de uma correspondencia
print(match.end()) #mostra o fim
    #split com expressões regulares
split_term = '@'
phrase = 'what is the domain name of someone with the email: hello@mail.com'
re.split(split_term,phrase)
    #encontrando todas as intãncias de um padrão
re.findall('match','test phrase math is in middle')
