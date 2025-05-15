lista =  [30, 22, 25, 28, 31, 27, 29]

print(lista)
print("=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-")

for i in range (len(lista)):
    if lista[i] < 25:
        lista[i] += 5

print(lista)
