contador = 0


while contador != 3:
    usuario = input("digite o seu login: ")
    senha = int(input("digite a senha: "))
    contador += 1

    if senha == 123 and usuario == "admin":
        print("login autotizado")
        contador = 3
    elif contador <3 and senha != 123:
        print("senha ou usuario incorretos! ")
    elif contador < 3 and usuario != "admin":
        print("senha ou usuario incorretos! ")
    if contador == 3 and senha != 123 and usuario != "admin":
        print("conta bloqueada")
