print("Ejemplo de Listas")
arcoiris=["Verde","Azul","Morado"]
print(arcoiris)
Longitud=(len(arcoiris))
print("Colores en el arcoiris:", Longitud)
print(f"Colores en el arcoiris: {Longitud}", "\n""El primer color del arcoiris es:",arcoiris[0])
print(f"El primer color del arcoiris es {arcoiris[0]}")
arcoiris.append("Rojo")
print(arcoiris)
Frutas=["Papaya","Piña"]
arcoiris.extend(Frutas)
print(arcoiris)
for olave in arcoiris:
    print(olave)