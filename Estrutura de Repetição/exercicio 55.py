#faça um programa que leia o peso de cinco pessoas. no final. mostre qual foi o maior e o menor peso lido

maior = 0
menor = 0
 
for i in range(1,6):
    peso = float(input('digite o peso da {} pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    else:
       if peso > maior:
          maior = peso
       if peso < menor:
          menor = peso
print(f'o maior peso lido foi de {maior} kg')
print(f'o menor peso lido foi de lido foi de {menor}kg')










