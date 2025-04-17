valort = 0
valorp = None

 

while valorp != 0 :
    valort = int(input("digite o valor da compra: "))
    valorp = (int(input("digite a quantia entregue para pagar: ")))

    if valort < valorp :
        print("saldo insuficiente")
    if valorp >= valort: 
        troco = valorp - valort
        nota100 = troco // 100
        troco %= 100 
        nota50 =  troco // 50 
        troco %= 50
        nota20 = troco // 20 
        troco %= 20
        nota10 = troco // 10
        troco %= 10
        nota5 = troco // 5
        troco %= 5
        nota2 = troco // 2
        troco %= 2
        print("notas de 100R$: ", nota100)
        print("notas de 50R$: ", nota50)
        print("notas de 20R$: ", nota20)
        print("notas de 10R$: ", nota10)
        print("notas de 5R$: ", nota5)
        print("notas de 2R$: ", nota2)
    else:
        print("saldo insuficiente")
