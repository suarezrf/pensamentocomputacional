lista = []
count = 0


while count < 10:
    num = int(input("digite numero: "))
    count += 1
    lista.append(num)
    menor = lista[0]
    maior = lista[0]

    if menor < num:
        menor += num
    elif maior > num:
        maior += num
print(lista)
print(menor)
print(maior)


