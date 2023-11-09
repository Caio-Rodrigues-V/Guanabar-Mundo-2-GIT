#faça um programa que mostre na tela uma contagem regressiva para o estouro de 10 fogos, indo de 10 a 0m com uma pausa de 1 segundo entre elas
from time import sleep
for numero in range(10,-1,-1):
    sleep(1)
    print(numero)