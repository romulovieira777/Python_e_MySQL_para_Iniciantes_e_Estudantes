while True:
    nomeProduto = input("Insira a descrição do produto: ")
    quantidade = int(input("Insira a quantidade do produto em estoque: "))
    continuar = input("Deseja cadastrar mais um produto? Sim[S] ou Não[N] ").lower()
    print(continuar)
    if continuar == "n":
        break

print(f"Produto {nomeProduto}")
print(f"Quantidade em estoque: {quantidade}")
