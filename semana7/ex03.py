lista = []
idade = None
soma = 0 

while idade != 0:
    idade = int(input("digite idade: "))
    if idade > 0:

        soma += idade

        lista.append(idade)

        print(lista)
        
soma /= len(lista)
print(soma)


