n1 = 0
n2 = 1
n3 = 0

contador = 0

termo = int(input("digite quantos termos da sequencia você deseja ver: "))

while contador != termo:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    contador += 1
