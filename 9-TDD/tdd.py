def sum(x, y):
    assert isinstance(x, (int, float)), 'x precisa set int ou float'
    assert isinstance(y, (int, float)), 'y precisa set int ou float'
    return x + y

try:
    print(sum("14", 5))
except AssertionError as e:
    print(f"Conta invalida: {e}")

print('Conta', sum(25, 25))