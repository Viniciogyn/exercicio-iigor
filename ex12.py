print("-------------------------------")
print("maior de 3 numeros")
print("-------------------------------")

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro numero: "))

maior = n1

if n2 > maior and n2 > n3:
    print(n2," e o maior numero!")
elif n3 > maior and n3 > n2:
    print(n3,"e o maior numero!")
else:
    print(n1,"e o miaor numero!")