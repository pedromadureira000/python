#!/usr/bin/env python3
# -*- coding: cp1252 -*-

'''
Para declarar uma codifica��o diferente da padr�o, uma linha de coment�rio especial deve ser adicionada como primeira
linha do arquivo. A sintaxe � essa:
# -*- coding: encoding -*-
Exemplo:
# -*- coding: cp1252 -*-

Uma exce��o para a regra da primeira linha � quando o c�digo-fonte inicia com uma linha com UNIX �shebang�. Nesse caso,
a declara��o de codifica��o deve ser adicionada como a segunda linha do arquivo. Por exemplo:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-
'''

#shebang: muda o interpretador python