print("--------------------------------")
print(" media com boletim ")
print("--------------------------------")

n1 = float(input(" Digite a nota do primeiro trimeste: "))
n2 = float(input(" Digite a nota do segundo trimeste: "))
n3 = float(input(" Digite a nota do terceiro trimeste: "))
n4 = float(input(" Digite a nota do quarto trimeste: "))

media = (n1+n2+n3+n4)/4

if media >= 70:
    print("parabens voce foi aprovado, com a media de: ",media)
elif media >= 50:
    print(" Se esforce mais, voce esta de recuperaçao com a media de: ",media)
else:
    print("Infelizmente voce foi reprovado, sua media foi: ",media)