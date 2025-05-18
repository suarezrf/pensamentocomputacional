lista = []
lista_tarefas_concluidas = []
count = 0

while count != 1:
    print("=== MENU ===")
    print("[1] Adicionar nova tarefa")
    print("[2] Listar tarefas")
    print("[3] Concluir tarefa")
    print("[4] Editar tarefa pendente")
    print("[5] Excluir tarefa pendente")
    print("[6] Sair")

    try:
        op = int(input("Escolha uma opção: "))
    except:
        print("> Numero invalido!")

    if op == 1:

        tarefa = input("> Digite a nova tarefa: ")
        lista.append(tarefa)
        print("> Tarefa adicionada com sucesso!")

    elif op == 2:
        print("====TAREFAS====")
        for i in range (len(lista)):
            print(f"{i + 1} {lista[i]}")
        print("=-=-=-=-=-=-=--=-=-=-=-==-=-=-")
        print()
        print("=--=-=-=-=-=- TAREFAS CONCLUIDAS =-=-=-=-=-=-")
        for i in range (len(lista_tarefas_concluidas)):
            print(f"{i + 1} {lista_tarefas_concluidas[i]}✅")
        print()

    elif op == 3:

        for i in range (len(lista)):
            print(f"{i+1}, {lista[i]}")
        select = int(input("> digite a tarefa que você deseja concluir: "))
        print(f"> A tarefa  {lista[select - 1]} foi concluida ✅")
        lista_tarefas_concluidas.append(lista[select-1])
        print("tarefa concluida com sucesso!")
        lista.pop(select - 1)

    elif op == 4:

        for i in range (len(lista)):
            print(f"{i+1}, {lista[i]}")
        select = int(input("selecione o item que você deseja editar: "))
        lista.pop(select - 1)
        edit = input("Digite o novo texto: ")
        lista.insert(select - 1, edit)
        print("> Tarefa editada com sucesso!")

    elif op == 5:
        for i in range (len(lista)):
            print(f"{i+1}, {lista[i]}")
        numero = int(input("Digite o número da tarefa que deseja excluir: "))
        print(lista[numero - 1], "a tarefa foi deletada com sucesso!")
        lista.pop(numero -1)

    elif op == 6:
        print("Você saiu do sistema!")
        count += 1
    
    
    else:
        print("> Opção inválida! Escolha de 1 a 6.")
