#Faça um programa que mostre a tabuada de vários numeros, um de cada vez, para cada valor digitado pelo usuario.
#O programa deve ser interrompido quando o numero solicitado for negativo
cont = 1

while True:
    n = int(input("Digite o numero que deseja consultar da tabuada: "))
    if n < 0:
        break
    for cont in range(1,11):
        resultado = n * cont
        print(f'{n} x {cont} = {resultado}')
        