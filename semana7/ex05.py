lista = []
lista1 = []
lista2 = []

count = 0
count1 = 0

while count != 5:
    num1 = int(input("digite a primeira lista de numeros: "))
    lista.append(num1)
    count += 1

print()
while count1 != 5:
    num2 = int(input("digite a segunda lista de numeros: "))
    lista1.append(num2)
    count1 += 1

for i in range (0,5):
    lista2.append(lista[i])

for i in range (0,5):
    lista2.append(lista1[i])

    
print(lista)
print(lista1)
print(lista2)
