#faça um programa que leia o primeiro termo e a razão de uma pa, mostrando os 10 primeiros termos da progressao usando estrutura while


razao = int (input ("Digite a razão da PA: "))
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
termo = primeiro_termo
mais = 10
total = 0
c = 1
while mais != 0:
    total = total + mais
    while c <= total:
        
        print(f"{termo} > ", end = '')
        termo += razao
        c = c + 1
    mais = int(input('quantos termos vc quer mostrar a mais? '))
total = c - 1
print(f"Voce mostrou um total de {total}")
# melhore o codigo acima e pergunte ao usuario se ele quer mostrar mais termos
# mostrando no final a quantidade de termos

