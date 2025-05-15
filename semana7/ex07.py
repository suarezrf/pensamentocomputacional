lista1 = []
lista2 = []
count = 0

while count != 10:
    numeros =  int(input(f"digite o numero: "))
    count += 1

    if numeros % 2 == 0 :
        lista1.append(numeros)

    else:
        lista2.append(numeros)

print(lista1)
print(lista2)
