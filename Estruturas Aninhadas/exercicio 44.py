#elabora um programa que calcule o valor a ser pago por um produto considerando o seu preço normal e a condição de pagamento
# a vista dinheiro ou chque - 10% de desconto
# a vista no cartao - 5% de desconto
# ate em 2x no cartão, preço normal
# 3x ou mais - 20% de juros

print("bem vindo\n")

preco_produto = float(input('qual o valor do item que o senhor quer comprar? '))
print('Escolha a forma de pagamento\n')
print('1 - A Vísta - 10% de desconto\n')
print('2 - A Vísta no Cartão - 5% de desconto\n')
print('3 - Em até 2x no cartão preço normal\n')
print('4 - em 3x ou mais - 20 de juros\n')

forma_pagamento = int(input('\nEscolha a forma de pagamento: '))

if forma_pagamento == 1:
    print('\nPagamento a vista ')
    print(f'esse é o valor do produto sem desconto {preco_produto}')
    desconto = preco_produto * 0.10
    produto_desconto = preco_produto - desconto
    print(f'esse é o preço com 10% de desconto {produto_desconto}')

elif forma_pagamento == 2:
    print("\nPagamento a vista com cartão")
    print(f'Esse é o valor inteiro sem desconto {preco_produto}!')
    desconto = preco_produto * 0.05
    produto_desconto = preco_produto - desconto
    print(f'Esse é o valor do produto com 5% de desconto {produto_desconto}')

elif forma_pagamento == 3:
    print('\nPagamento em 2x no cartão')
    print(f'Você pagará o preço inteiro da compra sem descontos ou juros, no valor de {preco_produto}')

elif forma_pagamento == 4:
    print('Pagamento em 3x ou mais no cartão, resultando em juros de 20% ')
    juros = preco_produto * 0.20
    produto_juros = preco_produto + juros
    print(f'Esse é o preço que você irá pagar com 20% de juros {produto_juros}')