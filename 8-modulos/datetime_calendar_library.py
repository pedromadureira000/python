import calendar
from datetime import datetime, timedelta

date = datetime(2021, 7, 7)  # pode declarar apenas ano, mes e dia
date = datetime(2021, 7, 7, 6, 49, 20)  # ano, mes, dia , hora, minuto, segundo


print(date.strftime('%d/%m/%Y %H:%M:%S'))

# esssa função vai receber uma string e um formato de data
print(datetime.strptime('20/04/2019', '%d/%m/%Y'))

# ver o timestamp
print(date.timestamp())

# converter timestamp para data
print(datetime.fromtimestamp(1555729200.0))

# adicionar tempo a uma data
date = datetime.strptime('20/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
print(date + timedelta(days=5))
print(date + timedelta(hours=10))
print(date + timedelta(seconds=59*60))

# é possivel tirar a diferença entre duas datas subtraindo elas
date = datetime.strptime('20/04/2020 20:00:00', '%d/%m/%Y %H:%M:%S')
date2 = datetime.strptime('20/04/2019 20:00:00', '%d/%m/%Y %H:%M:%S')
dif = date - date2
print(dif)
print(dif.total_seconds())
print(dif.days)

# comparações

print(date > date2)
print(date == date2)

# ver a data atual
print(datetime.now())

# data em ingles
dt = datetime.now()
formatacao = dt.strftime('%A, %d de %B de %Y')
print(formatacao)

# formatação de data em portugues _____________________________________

from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')

dt = datetime.now()
formatacao = dt.strftime("%A, %d de %B de %Y")
print(formatacao)

# ultimo dia do mes (quantos dias tem o mes)

from calendar import mdays  # lista com o ultimo dia de cada mes. Sendo o mes iqual ao indice de 1 - 12
# Leap year: Nao vai funcionar em ano bissexto
mes_atual = int(datetime.now().strftime('%m'))
print(mes_atual, mdays)
print(mes_atual, mdays[mes_atual])

# dia da semana do primeiro dia do mes(-1) e numero de dias no mes.
from calendar import monthrange, isleap
print(monthrange(2021, 2))
print(isleap(2021))

# lista com ultimo dia do ano com compreensao de lista (nao vai ter problema de ano bissexto)

ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
