import json
"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None
"""
# ----/convertendo de python para json
dict_clients = {1: {'nome': 'Luiz Otávio','sobrenome': 'Miranda','idade': 25,'altura': 1.80,'peso': 80.53,},2: {'nome': 'Maria','sobrenome': 'Oliveira','idade': 52,'altura': 1.67,'peso': 57,},3: {'nome': 'Pedro','sobrenome': 'Faria','idade': 32,'altura': 1.95,'peso': 113,},}
dados_json = json.dumps({"key": "value"}, indent=4)
print(dados_json, type(dados_json))

# ----/convertendo de json para python
json_clients = """{"1": {"nome": "Luiz Ot\u00e1vio","sobrenome": "Miranda","idade": 25,"altura": 1.8,"peso": 80.53},"2": {"nome": "Maria","sobrenome": "Oliveira","idade": 52,"altura": 1.67,"peso": 57},"3": {"nome": "Pedro","sobrenome": "Faria","idade": 32,"altura": 1.95,"peso": 113}}"""
dictionary = json.loads(json_clients)
print(dictionary, type(dictionary))

# ----/convertendo um dicionario para json e salvando em um arquivo
with open('clients.json', 'w') as file:
    json.dump(dict_clients, file, indent=4)

# ----/ convertendo json de um arquivo pra dicionario e salvando em uma variavel
with open('clients.json', 'r') as file:
    data = json.load(file)

for key, value in data.items():
    print(key)
    print(value)