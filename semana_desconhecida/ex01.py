
def numeros(lista):
    for i in range(10):
        numero = int(input(f"{i + 1}. digite numero: "))
        lista.append(numero)
    print("numeros na lista", lista)
    return lista

def somar(lista):
    soma = 0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            soma += lista[i]
    return soma

    

def main():
    lista = []
    numerico = numeros(lista)
    soma1 = somar(numerico)

    print(soma1)




main()
