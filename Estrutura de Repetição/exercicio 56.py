#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas, no final do programa mostre:
# A média de idade do grupo;
# Qual é o nome do homem mais velho.
# Quantas mulheres tem menos de 20 anos.

soma = 0
media = 0
maior = 0
nomevelho = ''
mulher20 = 0
for c in range(1, 5):
    print('---- {}ª PESSOA ----'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()[0]
    soma += idade
    if c == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    elif sexo in 'Mm' and idade > maior:
        maior = idade
        nomevelho = nome
    elif sexo in 'Ff' and idade < 20:
        mulher20 += 1
media = soma / 4
print('A média de idade do grupo é de {} anos'.format(media))
print('O homem mais velho tem {} anos e se chama {}'.format(maior, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))