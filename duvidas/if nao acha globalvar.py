string = "carrro"
strordenada = sorted(string)
caracter_anterior = strordenada[0]
counter = 1
def contador(string: str) -> str:
    print(strordenada)
    for caracter in strordenada[1:]:
        if caracter == caracter_anterior:
            counter += 1

        else:
            print(counter,caracter_anterior)
            caracter_anterior = caracter
            counter = 1


contador(strordenada)


