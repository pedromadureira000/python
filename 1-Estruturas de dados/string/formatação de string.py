     #%d inteiro , %s string , %a variavel (a)
     #%.2f float pegando 2 numeros apos a virugla
a = 'palavra'
print('essa é a %s'%a) #substitui %s pela variavel (a)
b= 10/3
print('essa é uma %.2f'%b) #mostra o numero da variavel (b) com duas casas apos a #virgula
print('float  %10.5f'%(12.444)) #o numero da esquerda é a qtd minima de caracteres que #vai ocupar (não podendo ser menor q o numero em si), o numero da direita é q qtd de #casas apos a virgula.
print('numero %s, string %s'%(123.1,'texto')) #use %s pra converter numero
print('one {p},two,{a},three{c},'.format(p=1,a="2",c=3)) #insere as 1-variaveis (p,a,c)
print("a \n notas da turma foram {}:".format(a)) #substitui variavel"