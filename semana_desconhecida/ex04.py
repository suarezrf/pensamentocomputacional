
def calcular(lista):
    for i in range (0, 8):
        numeros = int(input(f"{i + 1}. digite notas: "))
        lista.append(numeros)


def media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    soma /= 8
    return soma

def acima(soma,lista,lista2):
    for i in range(len(lista)):
        if lista[i] > soma:
            lista2.append(lista[i])
    for i in range (len(lista2)):
        print(f"Notas acima de {soma}: {lista2[i]}")


def main():
    lista = []
    lista2 = []
    calcular(lista)
    soma = media(lista)
    acima(soma,lista,lista2)


main()
