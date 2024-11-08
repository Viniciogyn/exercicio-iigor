print("------------------------------------")
print("Calculo de imc")
print("------------------------------------")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua Altura: "))

if peso <= 0:
    print("Sua peso nao pode ser menor ou igual a zero")
elif altura <= 0:
    print("Sua altra nao pode ser igual a zero")
else:
    print("vamos calcular seu IMC:")
    
imc = peso / (altura ** 2)

if imc < 18.5:
    print(" Seu IMC é de: ",imc,"Com este IMC voce esta dentro do seu peso normal!")
elif imc >= 18.5 and imc < 25:
    print(" seu IMC é de: ",imc,"Com este IMC voce esta acima do peso!")
else:
    print("seu IMC é de: ",imc,"Com este IMC voce esta com obesidade!")