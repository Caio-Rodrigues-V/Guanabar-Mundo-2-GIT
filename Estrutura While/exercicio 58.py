#Melhore o jogo do desafio 28 onde o computador vai penjsar em um numero entre 0 e 10. só que agora o jogar vai tentar adivinhar até acertar
#Mostrando no final quandos palpites o foram necessarios para vencer

import random
palpite = 0
computador = random.randint(0,10)
print("Ja pensei.")
acertou = False
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpite +=1
    if jogador == computador:
        acertou = True
    if jogador < computador:
        print('Tente um pouco mais alto')
    else:
        print('Tente um pouco mais baixo')
    
print('Acertou')
print(f'Você jogou {palpite} vezes')
