print("-----------------------------")
print(" Desconto de compra")
print("------------------------------")

valor = float(input("Digite o valor total da sua compra: "))
desconto = valor - (valor * 0,10)

if valor >= 100:
    print("o valor total da sua compra e de: R$",valor,"porem com o desconto o valor passa a ser: R$",desconto)
else:
    print(" o valor total da sua compra e de: R$",valor)