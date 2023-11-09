total_gasto = 0
produto_mais_barato = None
preco_mais_barato = float("inf")  # Inicializa o preço mais barato com infinito positivo
produtos_1000 = 0
while True:
    # Crie um programa que leia o nome e o preço de vários produtos
    produto = input("Digite o nome do produto: ").strip()
    preco_produto = input("Digite o preço do produto: ")

    if not preco_produto.replace(
        ".", "", 1
    ).isdigit():  # Verifica se o preço é um número
        print("Preço inválido. Por favor, insira um valor numérico.")
        continue

    preco_produto = float(preco_produto)

    # A) Qual é o total gasto na compra.
    total_gasto += preco_produto
    print(f"Total gasto até agora: R${total_gasto:.2f}")

    # B) Quantos produtos custam mais de R$ 1000.
    if preco_produto > 1000:
        produtos_1000 += 1

    # C) Qual é o nome do produto mais barato.
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = produto

    continuar = input(
        "Deseja adicionar mais produtos? (Digite 's' para sim, 'n' para não): "
    ).strip()
    if continuar.lower() != "s":
        break

print(f"O total gasto na compra é: R${total_gasto:.2f}")
print(f"Produtos que custam mais de R$ 1000: {produtos_1000}")
if produto_mais_barato is not None:
    print(f"O nome do produto mais barato é: {produto_mais_barato}")
else:
    print("Nenhum produto inserido ou todos os preços foram inválidos.")
