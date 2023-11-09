#escreva um programa que leia dois numeors inteiros e compare-os mostrando na tela uma mensagem
# o primeiro valor é maior
# o segundo valor é maior
# os odis sao iguals

n1 = int(input("Digite um numero: "))
n2 = int(input('digite outro valor: '))

if n1 > n2:
    print(f'o primeiro numero éo maior')
elif n2 > n1:
    print(f"o segundo numero é o maior")
elif n1 == n2:
    print('sao iguais')