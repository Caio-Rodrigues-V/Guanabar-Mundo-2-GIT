"""
- Escreva um programa para aprovar o emprestimo bancário para comprar uma casa.
- Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
- A prestação mensal não pode exceder 30% do salário ou então o emprestimo é negado.

"""

valor_casa = float(input("Digite o valor da casa em R$: "))
salario = float(input("Digite seu salário: "))
anos_pagar = float(input('quantos anos deseja pagar?'))

# Calculando o valor das prestações mensais
prazo_meses = anos_pagar * 12
prestacao_mensal = valor_casa / prazo_meses

#calculando o limite de 30% do salario
limite_prestacao = salario * 0.3

#verifica se a prestacao mensal está dentro do limite
if prestacao_mensal <= limite_prestacao:
    print("Emprestimo aprovado! pestação mensal: R$ {:.2f}".format(prestacao_mensal))
else:
    print("Emprestimo negado! ")