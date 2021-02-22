#!/usr/bin/env python3
# -*- coding: cp1252 -*-


'''
Para declarar uma codificação diferente da padrão, uma linha de comentário especial deve ser adicionada como primeira
linha do arquivo. A sintaxe é essa:
# -*- coding: encoding -*-
Exemplo:
# -*- coding: cp1252 -*-

Uma exceção para a regra da primeira linha é quando o código-fonte inicia com uma linha com UNIX “shebang”. Nesse caso,
a declaração de codificação deve ser adicionada como a segunda linha do arquivo. Por exemplo:

#!/usr/bin/env python3
# -*- coding: cp1252 -*-

'''

#shebang: muda o interpretador python