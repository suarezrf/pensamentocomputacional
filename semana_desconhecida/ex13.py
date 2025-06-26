
# 13. Cofrinho digital

# Você foi contratado para programar o sistema de um cofrinho digital para ajudar crianças a controlarem suas economias.
# Cada vez que uma criança guarda um valor, esse valor é registrado em uma lista.
# O sistema precisa oferecer um menu com as seguintes opções:

# === Cofrinho Digital ===
# 1. Adicionar valor ao cofrinho
# 2. Ver todos os valores guardados
# 3. Ver o total economizado
# 4. Ver quantas vezes um valor específico foi guardado
# 5. Retirar o valor mais recente adicionado
# 6. Sair

# O sistema deve funcionar em um laço while, exibindo o menu após cada operação, até que o usuário escolha a opção 6 para sair.
# A opção 1 deve solicitar um valor positivo e adicioná-lo à lista.
# A opção 2 exibe todos os valores guardados, na ordem em que foram adicionados.
# A opção 3 calcula e exibe a soma total dos valores guardados.
# A opção 4 deve solicitar um valor ao usuário e contar quantas vezes ele aparece na lista.
# A opção 5 remove o último valor adicionado (se houver) e informa qual foi removido.
def menu():
    print("------=== Cofrinho Digital ===------")
    print("1. Adicionar valor ao cofrinho")
    print("2. Ver todos os valores guardados")
    print("3. Ver o total economizado")
    print("4. Ver quantas vezes um valor específico foi guardado")
    print("5. Retirar o valor mais recente adicionado")
    print("6. Sair")
    opc = int(input("selecione umas das opções:  "))
    return opc

def adicionar(lista):
    numero = int(input("> adicione um valor ao seu cofre: "))
    lista.append(numero)
    return lista

def ver(lista):
    for i in range (len(lista)):
        print(f"{i + 1}. {lista[i]}")

def soma(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    print(soma)

def verificar(lista):
    quantia = 0
    numero = int(input("> verificar quantas vezes essse numero foi adicionado ao seu cofre: "))
    for i in range (len(lista)):
        if numero == lista[i]:
            quantia += 1
    print(f"> quantia de vezes que você adicionou o numero {numero} a seu cofre")
    print("> ", quantia)


def remove(lista):
    print("> cofre antes")
    print(lista)
    lista.pop()
    print("cofre depois")
    print(lista)


def main():
    count = 0
    lista = []
    while  count != 1 :
        opc = menu()
        if opc == 1:
            add = adicionar(lista)
        elif opc == 2:
            ver(lista)
        elif opc == 3:
            soma(lista)
        elif opc == 4:
            verificar(lista)
        elif opc == 5:
            remove(lista)
        elif opc == 6:
            count += 1
            print("> você saiu do sistema!")
        else:
            print("> numero invalido! ")

main()
