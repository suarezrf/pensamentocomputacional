

def nome_idade(nomes,idades):
    print("-=-=-=--=-=-=- cadastro -=-=-=-=-=-=-")
    nome = input("digite nome: ")
    idade = int(input("digite idade: "))
    nomes.append(nome)
    idades.append(idade)

    return nomes,idades


def remove(nomes, idades):
    print("-=-=-=-=-=-=--=-=- CADASTROS =--=-=-=-=-=-=--=-")
    print()
    for i in range (len(nomes)):
            print(f"> {i + 1}. nome do participante:", nomes[i],  "     > idade do participante:",idades[i])
    print()
    print("=-=-=-=-=-==-=-= REMOVER CADASTROS =-=-=---==--=-=")
    
    nome = input("digite o nome da pessoa cadastrada: ")
    for i in range (len(nomes)):
        if nomes[i] == nome:
            nomes.remove(nomes[i])
            idades.remove(idades[i])
    print()
    print("=-=-=-=-=-=-==- LISTA APÓS A REMOÇÃO DO CADASTRO =-=-=--=-=-=-")
    print(nomes)
    print(idades)

    return nomes,idades


def listar(nomes,idades):
    for i in range (len(idades)):
        if idades[i] <= 18:
            print()
            print("-=-=-=-=-=-=-=-=- PARTICIPANTES COM 18 ANOS OU MENOS =-=-=-=-=--==-=-")
            print("> nome do participante:", nomes[i],  "     > idade do participante:",idades[i])
        


def media_idade(nomes,idades):
    soma = 0
    for i in range (len(idades)):
        soma += idades[i]
    individuos = len(idades) 
    media = soma / individuos
    print("=-=--=-=-=-=-= MÉDIA DAS IDADES =-=--=-=-=-=-=-")
    print("media: ",media)
    print("quantia de participantes", len(nomes))
    mais_velho = idades[0]
    for i in range (len(idades)):
        if idades[i] > mais_velho:
            mais_velho = idades[i]
            nome = nomes[i]
    print("particante mais velho:", nome, "> idade do participante: ", mais_velho)


def maior(nomes,idades):
    for i in range (len(idades)):
        if idades[i] > 18:
            print()
            print("-=-=-=-=-=-=-=-=- PARTICIPANTES COM MAIS DE 18 ANOS =-=-=-=-=--==-=-")
            print("> nome do participante:", nomes[i],  "     > idade do participante:",idades[i])

def main():
    nomes = []
    idades = []
    count = 0
    while count != 1:
        print()
        print("-=-=-=-=-=-= MENU =-=-=-=-=-=-=-")
        print("1. Cadastrar participante ")
        print("2. remover participante")
        print("3. listar participantes")
        print("4. mostrar estatisticas")
        print("5. Mostrar participantes maiores de idade (18+)")
        print("6. sair ")
        try:
            opc = int(input("selecione uma das opções: "))
        except:
            print("=-=---=-=- OPÇÃO INVALIDA =-=-=-=-=-=")

        if opc == 1:
            nomes, idades = nome_idade(nomes,idades)

        elif opc == 2:
            nomes, idades = remove(nomes,idades)

        elif opc == 3:
            listar(nomes,idades)
        
        elif opc == 4:
            media_idade(nomes,idades)

        elif opc == 5:
            maior(nomes,idades)

        elif opc == 6:
            count += 1
            print("=-=-=-=-=-=--=-=- você saiu do sistema -=-=-=-=--=-=-")
        
        else:
            print("opção invalida!")
            
        
main()
