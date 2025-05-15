lista1 = []
lista2 = []
lista3 = []
count = 0

print("digite numeros para nossa primeira lista")
while count != 5:
    num1 = int(input("digite numero: "))
    lista1.append(num1)

    count += 1 

print("digite numeros para nossa segunda lista")

count = 0

while count != 5:
    num2 = int(input("digite numero: "))
    lista2.append(num2)

    count += 1

for i in range (0,5):
    if lista1[i] in lista2 :
        
        lista3.append(lista1[i])

print(lista1)

print(lista2)

print(lista3)


