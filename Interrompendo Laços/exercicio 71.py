# Crie um programa que simule o funcionamento de um CAIXA ELETRONICO
# No inicio, pergunte ao usuário qual será o valor a ser sacado(numero inteiro)
# E o programa vai informar quantas cedulas de cada valor serão entregues.

# OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE 50 20 10 E 1

saque = int(input("Digite quanto você deseja sacar: "))

cedula_50 = saque // 50
saque %= 50

cedula_20 = saque // 20
saque %= 20

cedula_10 = saque // 10
saque %= 10

cedula_1 = saque

print("Entregar:")
if cedula_50 > 0:
    print(f"{cedula_50} cédulas de R$50")
if cedula_20 > 0:
    print(f"{cedula_20} cédulas de R$20")
if cedula_10 > 0:
    print(f"{cedula_10} cédulas de R$10")
if cedula_1 > 0:
    print(f"{cedula_1} cédulas de R$1")
