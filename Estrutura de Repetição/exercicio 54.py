#crie um programa que leia o ano de nascimento de sete pessoas. no final, mostre quiantas pessoas ainda nao atingiram maioridade

tot_maior = 0
tot_menor = 0
for i in range(1,8):
    ano = int(input("Digite o seu ano de nascimento: "))
    idade = 2023- ano
    if idade < 18:
        print("Voce ainda é menor de idade")
        tot_menor += 1
    else:
        print("Você é amior de idade")
        tot_maior += 1

print(f"O total de pessoas que ainda não atingiram a maioridade é {tot_menor}")
print(f"O total de pessoas que atingiram a maioridade é {tot_maior}")