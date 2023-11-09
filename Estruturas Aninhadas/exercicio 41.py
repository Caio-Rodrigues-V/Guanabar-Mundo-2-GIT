# a confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos - mirim
# até 14 anos - infantil 
# ate 19 anos - junior
# até 20 anos - senior
# acima - master

ano = int(input('Digite seu ano de nascimento: '))

idade = 2023 - ano

if idade <= 9:
    print(idade)
    print('Você é da categoria MIRIM')

elif idade <= 14:
    print(idade)
    print('Você é da categoria infantil')

elif idade <= 19:
    print(idade)
    print('Você é da categoria junior')

elif idade == 20:
    print(idade)
    print('você é da categoria senior')
else:
    print(idade)
    print("voce ja e´um master")
