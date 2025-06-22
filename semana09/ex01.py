
def mostrar_menu():
    print("=-=-=-=-=-== MENU ==-=-=-=-=-=-=")
    print("[1] Adicionar nova tarefa")
    print("[2] Listar tarefas")
    print("[3] Concluir tarefa")
    print("[4] Editar tarefa pendente")
    print("[5] Excluir tarefa pendente")
    print("[6] Sair")

def adicionar_tarefa(lista):
    tarefa = input("> Digite a nova tarefa: ")
    lista.append(tarefa)
    print("> Tarefa adicionada com sucesso!")

def listar_tarefas(lista,lista_tarefas_concluidas):
    print("=-=-=-=-=-=-=-=-= TAREFAS =-=-=-=--=-=-=-=-=")
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
    print("=-=-=-=-=-=-=--=-=-=-=-==-=-=-\n")
    print("=--=-=-=-=-=- TAREFAS CONCLUIDAS =-=-=-=-=-=-")
    for i in range(len(lista_tarefas_concluidas)):
        print(f"{i + 1}. {lista_tarefas_concluidas[i]} ✅")
    print()

def concluir_tarefa(lista,lista_tarefas_concluidas):
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
    try:
        select = int(input("> Digite a tarefa que você deseja concluir: "))
        print(f"> A tarefa '{lista[select - 1]}' foi concluída ✅")
        lista_tarefas_concluidas.append(lista[select - 1])
        lista.pop(select - 1)
        print("Tarefa concluída com sucesso!")
    except:
        print("-=-=-=-=-= INVÁLIDO! =-=-=-=-=-=")

def editar_tarefa(lista):
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
    try:
        select = int(input("Selecione o item que você deseja editar: "))
        edit = input("Digite o novo texto: ")
        lista[select - 1] = edit
        print("> Tarefa editada com sucesso!")
    except:
        print("=-=-=-=-=-==-= INVÁLIDO =--=-=-=-=-=-=")

def excluir_tarefa(lista):
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}")
    try:
        numero = int(input("Digite o número da tarefa que deseja excluir: "))
        print(lista[numero - 1], "a tarefa foi deletada com sucesso!")
        lista.pop(numero - 1)
    except:
        print("=-=-=-=-=-=-=-= INVÁLIDO =-=-=-=-==-=-=-=")

def main():
    lista = []
    lista_tarefas_concluidas = []
    count = 0
    while count != 1:
        mostrar_menu()
        try:
            op = int(input("Escolha uma opção: "))
        except:
            print("> Número inválido!")
            continue

        if op == 1:
            adicionar_tarefa(lista)
        elif op == 2:
            listar_tarefas(lista,lista_tarefas_concluidas)
        elif op == 3:
            concluir_tarefa(lista,lista_tarefas_concluidas)
        elif op == 4:
            editar_tarefa(lista)
        elif op == 5:
            excluir_tarefa(lista)
        elif op == 6:
            print("-------= VOCÊ SAIU DO NOSSO SISTEMA! =--------")
            count += 1
        else:
            print("> Opção inválida! Escolha de 1 a 6.")

main()
