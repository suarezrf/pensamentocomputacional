
# Solicite ao usuário um número inteiro positivo. Gere a sequência de Collatz a partir desse número:
# se for par, divide por 2; se for ímpar, multiplica por 3 e soma 1.
#     Continue até que o número chegue a 1.Armazene todos os valores da sequência em uma lista e exiba-a.
def numero():
    try:
        numero1 = int(input("digite um numero inteiro: "))
    except:
        print("seu numero não é inteiro!")
    return numero1
def par_ou_impar(numero):
    lista = []
    while numero != 1:
        if numero % 2 == 0:
            numero /= 2
            lista.append(numero)
        else:
            numero *= 3 
            numero += 1
            lista.append(numero)
    print(lista)
    
def main():
    numero1 = numero()
    par_ou_impar(numero1)



main()
