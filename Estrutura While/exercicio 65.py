#Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução. mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ocntinuar ou nao a digitar numeros
soma = 0
maior = float('inf')
menor = float('inf')
contador = 0

while True:
    n = int(input("Digite um numero inteiro : "))
    soma = soma + n
    contador = contador + 1


    #atualizar o maior e menor

    if n > maior:
        maior = n
    if n < menor:
        menor = n 
    
    continuar = input("Deseja continuar? ").lower()
    if continuar != 's':
        break

if contador > 0:
    media = soma / contador
    print(f'Média {media}')
    print(f'Maior = {maior}')
    print(f'menor = {menor}')
else:
        print('nenhum numero foi digitado')