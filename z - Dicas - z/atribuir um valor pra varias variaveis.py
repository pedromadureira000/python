u = True
x = 1
y = 2
z = 3

z, y, x = u, u, u
print(z, x, y, z, u)
z = y = x = u
u = True
x = 1
y = 2
z = 3
z, x, y, u = 3, 1, 2, True
z = y = x = u     #a atribuição ocorre da direita pra esquerda, todos recebem "u"
print(z, x, y, u)