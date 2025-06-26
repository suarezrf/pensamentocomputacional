
# Peça ao usuário que digite 5 números inteiros para formar a primeira lista e,
# em seguida, mais 5 números para formar a segunda lista. Em seguida, calcule
# todas as somas possíveis entre os elementos das duas listas, combinando cada
# número da primeira com cada número da segunda. Armazene em uma nova lista apenas
# as somas que forem números pares, garantindo que cada valor apareça apenas uma vez.
# Ao final, exiba a lista contendo todas as somas pares distintas geradas a partir das combinações.


def calculo(lista1,lista2):
    lista3 = []

    for i in range (len(lista1)):

        for j in range (len(lista2)):
            soma = lista1[i] + lista2[j]

            if soma % 2 == 0:
                contador = 0

                for k in range (len(lista3)):
                    if lista3[k] == soma:
                        contador += 1
                        
                if contador == 0:
                    lista3.append(soma)
    print(lista3)

def chamar(lista1,lista2):
    print("=-=-=-=-=-= LISTA 1 =-=-=-=-=-=-=-")
    print()
    for i in range (0,5):
        n1 = int(input(f"{i + 1}. digite numero: "))
        lista1.append(n1)
    print()
    print("=-=-=-=-=-= LISTA 2 =-=-=-=-=-=-=-")
    print()
    for i in range (0,5):
        n2 = int(input(f"{i + 1}. digite numero: "))
        lista2.append(n2)

    return lista1,lista2

def main():
    lista1 = []
    lista2 = []
    lista1,lista2 = chamar(lista1,lista2)
    calculo(lista1,lista2)



main()
