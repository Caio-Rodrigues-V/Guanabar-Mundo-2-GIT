#Crie um programa que leia varios numeros inteiros pelo teclado.
# O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada
# no final mostre quantos numeros foram digitados e qual foi a soma entre eles.
n = 0
cont = 0
soma = 0 
while n != 999:
    n = int(input("Digite um numero: "))
    if n != 999:
        soma += n
        cont += 1
print(f'vc digitou {cont} numeros e a soma deles foi de {soma}')