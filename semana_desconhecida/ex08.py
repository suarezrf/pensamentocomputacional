def sla(lista):
    dois = 2
    for i in range (2,101):
        lista.append(dois)
        dois += 1
    print(lista)
    return lista

def verificar(lista):
    lista_nao_primos = []
    lista_primos = []

    for i in range (len(lista)):
        divisor = 0
        for j in range (1, lista[i] + 1):
            if lista[i] % j == 0 :
                divisor += 1
        if divisor == 2:
            lista_primos.append(lista[i])
        else:
            lista_nao_primos.append(lista[i])
    print("-=-=-=-=-=-==- NÃO SÃO NUMEROS PRIMOS ==--=-=-=--=-=-=-=-")
    print(lista_nao_primos)
    print("-=-=-=-=-=-==--=-=-= PRIMOS -=-==-==--=-=-=--=-=-=-=-")
    print(lista_primos)
                
            



def main():
    lista = []
    sla(lista)
    verificar(lista)

main()
