"""O interpretador Python se baseia em regras de nomes para determinar alguns comportamentos.
Existem trez formas de nomeação que tem significados especiais:
1.;Nomes começados e terminados com dois underscores: __*__
2.Nomes começados com um underscore: _*
3.Nomes começados com dois underscores: __*

__*__
Esses são nomes começados e terminados com dois underscores. Eles são conhecidos como "métodos dunder". "Dunder" significa "double underscore".

Exemplos: __init__ (lê-se "dunder init"), __next__ ("dunder next"), __getattr__, __del__, __str__, etc.

Qualquer identificador nomeado dessa forma, é considerado reservado para a linguagem Python.

Portanto, não crie variáveis, nem funções, nem métodos, nem classes, nem nada que o nome comece e termine com dois underscores. O manual avisa que isso pode causar problema de compatibilidade com a linguagem, sem nenhum aviso.

____________________________

_*
Nomes começados com um underscore, quando criados dentro de um módulo (ou pacote), não são importados quando usamos o comando from modulo import *.

Se você está criando um módulo e quer que alguma função, variável ou classe não seja importada automaticamente, nomeie-a iniciando com um underscore. Exemplo: _minha_funcao_interna().

Usando o mesmo conceito de "interno", métodos e variáveis internas de uma classe que não devem ser acessados de fora dela, também devem começar com um underscore. Mas isso não os torna privados. Nesse caso, é apenas uma convenção mesmo.

__________________________
__*
Nomes começados com dois underscores são fonte de erro de interpretação e foram eles que me motivaram a escrever esse post. Eles são nomes de métodos ou variáveis privados de uma classe.

Quando variáveis ou métodos com nomes assim são definidos dentro de uma classe, eles são modificados e têm o nome da classe inserido no início.

...muito complexo, para ver na integra acesse http://aprenda-python.blogspot.com/2013/05/um-ou-dois-sublinhados.html
...
interpretador modifica o nome de variáveis iniciadas com dois underscores: para protegê-los e torná-los realmente privados. Nada fora da classe onde eles foram criados pode acessá-los, a não ser que seja explicitamente,
se você quer criar uma classe e ela tem a possibilidade de ser extendida, não crie métodos nem variáveis iniciados com dois underscores. A não ser que você tenha certeza que eles nunca serão usados nas classes filhas.

"""