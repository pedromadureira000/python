import random
import string

# Gera um número inteiro entre  A e B
# inteiro = random.randint(10, 20)

# Gerar um número aleatório usando a função range()
inteiro = random.randrange(900, 1000, 10)

# Gera um número de ponto flutuante entra A e B
# flutuante = random.uniform(10, 20)

# Gera um número de ponto flutuante entre 0 e 1
flutuante = random.random()

lista = ['Luiz', 'Otávio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

# Seleciona aleatóriamente valores de uma lista
sorteio = random.sample(lista, 2)  # return 2 randown values from list (can't repeat)
# sorteio = random.choices(lista, k=2)  # return 2 randown values from list (can repeat)
# sorteio = random.choice(lista)  # choice just one value

# Embaralha a lista
random.shuffle(lista)
ascii_letters
# Gera senha aleatória
letras = string.ascii_letters  # return letter in uppercase and lowcase
# you could use ascii_uppercase and ascii_lowercase too
digitos = string.digits
caracteres = '!@#$%&*._-'
geral = letras + digitos + caracteres
senha = "".join(random.choices(geral, k=20))

print(senha)
