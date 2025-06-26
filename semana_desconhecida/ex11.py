# Peça ao usuário para informar uma base (número inteiro) e um expoente máximo.
# Crie uma função que retorna uma lista com todas as potências da base, do expoente 0 até o máximo informado. Exiba essa lista. 


def numero():
    try:
        numero = int(input("numero base: "))
    except:
        print("numero invalido!")
    return numero

def expoente():
    try:
        numero = int(input("numero do expoente: "))
    except:
        print("numero invalido!")
    return numero

def calculo(numero, expoente):
    lista = []
    for i in range (0,expoente + 1):
        conta = numero ** i
        lista.append(conta)
    print(lista)
def main():
    n1 = numero()
    n2 = expoente()
    calculo(n1,n2)


main()
