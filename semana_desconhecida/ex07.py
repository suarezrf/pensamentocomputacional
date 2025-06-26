# Peça ao usuário que digite 7 números inteiros e armazene-os em uma lista.
# O programa deve identificar o menor número da lista e o último número ímpar digitado, e calcular o produto entre eles.
# Exiba a lista, os dois valores encontrados e o resultado do produto.
def chamar(lista):
    for i in range (0,7):
        numero = int(input(f"{i + 1}. digite numeros: "))
        lista.append(numero)

    return lista

def verificar(lista):
    impar = 0
    menor = lista[0]
    for i in range (len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    
        if lista[i] % 2 != 0:
            impar = lista[i]
    print(menor)
    print(impar)

    return menor,impar

def produto(menor,impar):
    valor = menor*impar
    print(valor)

def main():
    lista = []
    chamar(lista)
    menor,impar = verificar(lista)
    produto(menor,impar)
    
main()
