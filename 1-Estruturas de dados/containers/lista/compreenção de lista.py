# A compreensão de listas nos permitem construir listas usando uma notação diferente. Vc pode pensar nisso essencialmente
# como um loop construido dentro de colchetes.

lst = [x for x in "string"]  #lista com caracteres
lst2=[x**2 for x in range(10)] #lista de x²
lst3=[x**2 for x in [x**2 for x in range(10)]] #aninhamento em compreensão de lista
lst4=[x**2 for x in range(10) if x % 2 ==0]  #flow control em list comprehension

print(lst,lst2,lst3,lst4)

#---exemplo----
celsius=[0,10,20.1,34.5]
fahrenheit = [((9/5)*temp+32) for temp in celsius]

