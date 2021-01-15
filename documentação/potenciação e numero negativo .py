# Uma vez que ** tem precedência mais alta que -, -3**2 será interpretado como -(3**2) e assim resultará em -9. Para evitar
# isso e obter 9, você pode usar (-3)**2.
print(-3**2)
print((-3)**2)