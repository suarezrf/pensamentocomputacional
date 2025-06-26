
import math

def quadrados_perfeitos():
    numeros = []
    perfeitos = []

    for i in range(10):
        n = int(input(f"{i + 1}. Digite um número inteiro: "))
        numeros.append(n)


    for numero in numeros:
        if numero >= 0:  
            raiz = math.sqrt(numero)
            if raiz.is_integer():
                perfeitos.append(numero)

    print("Números informados:", numeros)
    print("Quadrados perfeitos encontrados:", perfeitos)
