# Faça um programa que jogue par ou impar com o computador, o Jogo só será interrompido quando o jogador perder, mostrando o total de vitorias
# consecutivas que ele conquistou no final do jogo.
import random

vitorias = 0


while True:
    # Iniciando o numero do computador e os inputs do player.
    computador = random.randint(1, 100)
    escolha = input("Digite Par ou Impar [P/I]:").lower()
    player = int(input("Digite um numero: "))

    # Verificando a escolha do jogador, se for PAR ele ja entra nesse IF.
    if escolha == "par" or escolha == "p":
        resultado = player + computador
        # verifica se o resto da soma do input do player e do computador é resto 0, se for resto 0 é par
        if resultado % 2 == 0:
            print(
                f"Você jogou {player} e o Computador jogou {computador}, O resultado foi {resultado} sendo assim PAR! O Jogoador ganhou 👱"
            )
            vitorias += 1

        else:
            print(f"A escolha foi {resultado} e é IMPAR, o Computador Ganhou! 💻 ")
            print(f"O total de vitorias consecutivas pelo jogador foi de {vitorias}")
            break
    # Verifica a escolha do jogaro, se for Impar cai nesse elif
    elif escolha == "impar" or escolha == "i":
        resultado = player + computador
        # verifica se o resto da soma do input do player e do computador é resto 1, se for resto 1 é impar
        if resultado % 2 == 1:
            print(
                f"Você jogou {player} e o Computador jogou {computador}, O resultado foi {resultado} sendo assim Impar! O Jogoador ganhou 👱 "
            )
            vitorias += 1
        else:
            print(f"O Resultado foi {resultado} e é PAR, o Computador Ganhou! 💻")
            print(f"O total de vitorias consecutivas pelo jogador foi de {vitorias}")
            break
    else:
        print("Escolha invalida! ")
