#Crie um programa que faça o computador jogar jokenpô com você.
"""
Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).

"""

import random

print("Bem vindo ao jokenpo game!")

computador = ['Pedra',  'Papel',  'Tesoura' ]
computador_escolha = random.choice(computador)
escolha_player = input("Pedra ? Papel ? Tesoura? ").lower()

if escolha_player == 'pedra':
    if computador_escolha == 'tesoura':
        print('Player Ganhou! ')
    else:
        print('Computador Ganhou')
elif escolha_player == 'tesoura':
    if computador_escolha == 'Papel':
        print('Player Ganhou!')
    else:
        print('Computador Perdeu')
elif escolha_player == 'papel':
    if computador_escolha == 'Pedra':
        print('Player Ganhou')
    else:
        print('Computador Ganhou! ')
elif escolha_player == computador_escolha:
    print("Draw")
else:
    print("Opção invalida")