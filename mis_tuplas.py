print("Ejemplos de tuplas")
Canciones=("Te sigo amando","Si me dejas ahora","Desesperado")
print(Canciones)
y = list(Canciones)
y[1] = "Que lloro"
x = tuple(y)
print(x)
print(type(x))