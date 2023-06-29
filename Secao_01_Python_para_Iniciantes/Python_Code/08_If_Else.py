nomeCliente = input("Por favor insira o seu nome: ")
idadeCliente = int(input("Qual a sua idade: "))
renda = float(input("Informe a sua Renda Bruta Mensal: "))

if renda >= 2000:
    print("Parabéns, seu crédito foi aprovado!")
else:
    print("Infelizmente seu crédito não foi aprovado!")
