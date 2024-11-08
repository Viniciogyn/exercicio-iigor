print("-------------------------------")
print("Maioridade")
print("-------------------------------")

dia = int(input("Digite o dia da sua data de nascimento: "))
mes = input("digite o mes da sua data de nascimento: ")
ano = int(input("digite o ano do seu nascimento: "))

permissao = 2024 - ano
falta = 18 - permissao

if permissao >= 18:
    print("Você já tem", permissao, "anos de idade e ja pode dirigir! ")
else:
    print("voce tem",permissao,"anos de idade, e faltam",falta,"anos para voce dirigir!")

