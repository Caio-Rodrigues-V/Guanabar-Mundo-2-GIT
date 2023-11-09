#faça um programa que leia se ele é numero primo ou não
numero = int(input("Digite seu numero: "))
tot = 0
for i in range(1,numero + 1):
    if numero % i == 0:
        print('\033[34m', end = '')
        tot += 1
       
    else:
        print('\033[31m', end = '')
    print(f'{i}',end = ' ')
if tot <= 2:
    print('Numero é primo')
    print(f'o numero {numero} foi divisivel {tot} vezes')
else:
    print(f'\no numero {numero} foi divisivel {tot} vezes')
    print('entao nao é um primo')
    