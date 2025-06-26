# Solicite que o usuário digite 12 números inteiros. 
# Em seguida, peça mais um número para busca. 
# O programa deve informar a última posição (índice) em que esse número apareceu na lista. 
# Caso o número não esteja presente, uma mensagem adequada deve ser exibida.

def chamar(lista):
    for i in range(0, 12):
        numeros = int(input(f"{i + 1}. digite seu numero: "))
        lista.append(numeros)
    print(lista)
    return lista



def buscar(lista):
    posicao = -1
    numero = int(input("digite a posição do seu numero: "))
    for i in range (len(lista)):
        if lista[i] == numero:
            posicao = i 
    
    if posicao == -1:
        print("Seu numero não esta na lista! ")

    else:
        print("Seu numero está no indice :", posicao)


def main():

    lista = []
    chamar(lista)
    buscar(lista)

main()
