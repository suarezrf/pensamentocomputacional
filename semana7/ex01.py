lista = []
lista1 = []
count = 0
soma = 0
soma1 = 0


while count != 8:
    num1 = int(input("digite um numero: "))
    lista.append(num1)
    count += 1
    soma += num1


    if num1 > 30:
        lista1.append(num1)
        soma1 += num1
print(lista)
print(soma)
print(lista1)
print(soma1)




