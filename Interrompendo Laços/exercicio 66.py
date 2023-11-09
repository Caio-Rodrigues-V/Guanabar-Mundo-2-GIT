#crie um programa que leia varios numeros inteiros. O programa deve parar quando o usuario digitar 999
# no final mostre quantos numeros foram digitados e qual foi a soma entre eles desconsiderando a red flag
soma = 0
contador = 0
while True:
    n = int(input("Digite um numero: "))
    print(n)
    if n == 999:
        print('parando programa')
        break
    soma += n
    contador +=1
print(f'voce digitou {contador} numeros e a soma entre eles é de {soma}')

