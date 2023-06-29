nomeCliente = input("Por favor insira o seu nome: ")
idadeCliente = int(input("Qual a sua idade? "))
renda = float(input("Informe a sua Renda Bruta Mensal: "))

if renda >= 2000 and idadeCliente >= 18:
    print(f"Parabéns Sr(a) {nomeCliente}, seu crédito foi aprovado!")
else:
    print(f"Olá Sr(a) {nomeCliente}, infelizmente seu crédito não foi aprovado!")
