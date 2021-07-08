"""
Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...
"""
import csv

with open('clientes.csv', 'r') as arquivo:
    # we use a list compreension because the conection with file will be closed outside "with" statement
    # data_list = [x for x in csv.reader(arquivo)]  # reader is a generator(when i use it, data dict come blank)
    data_dict = [x for x in csv.DictReader(arquivo)]  # DictReader is a generator
    print(data_dict)

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL  # quotes all values.
    )

    chaves = data_dict[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in data_dict:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )