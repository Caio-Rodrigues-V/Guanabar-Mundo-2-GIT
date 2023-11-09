#faça um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram no intervalo de 1 a 500

numero = 0
for i in range(1,501):
    if i % 3 == 0:
        numero = numero + i
print(numero)