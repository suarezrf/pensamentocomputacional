def divisao(lista,lista1):
    for i in range (len(lista)):
        if lista[i] % 3 == 0 and lista[i] > 0:
            lista1.append(lista[i])
        else:
            print(lista[i], "não é multiplo de 3")
    print("lista de numeros que são multiplos por 3: ", lista1)


def chamar(lista):
    for i in range (0, 10):
        numeros = int(input(f"{i + 1}. digite seu numero: "))
        lista.append(numeros)
    return lista



def main():
    lista = []
    lista1 = []
    print("=-=-=-=-=-==-=-=-=-=-=-=-=")
    chamar(lista)
    print("=-=-=-=-=-==-=-=-=-=-=-=-=")
    divisao(lista,lista1)
    print("=-=-=-=-=-==-=-=-=-=-=-=-=")



main()

    
