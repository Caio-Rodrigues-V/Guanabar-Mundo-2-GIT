#crie um programa que leia duas notas de um alone e calcule sua media, mostrando uam mensagem no final, de acordo com a media atingida:
# media abaixo de 5 - repovrado
# media entre 5 e 5.9 - recuperação
# media acima de 7 - aprovado

n1 = float(input("digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2

if media < 5:
    print('reprovado filha da puta')
elif media >= 5 and media <= 5.9:
    print('recuperação')
else:
    print('aprovado')
