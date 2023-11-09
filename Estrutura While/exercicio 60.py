#faça um programa que leia um numero qualquer mostrando o seu fatorial
# ex 5! = 5x4x4x2x1
from math import factorial

while True:
    numero = int(input("Digite um numero que queira fatorar: "))

    fatorar = factorial(numero)
    print(fatorar)

    continuar = input("Dseja continuar fatorando numeros? ").lower()
    if continuar != 's':
        print("Encerrando programa")
        break