#reçaa o desafio 09, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando for

numero = int(input("que numero deseja checar a tabuada? "))

for i in range(1,11):
    resultado  = numero * i
    print(f'{numero } x {i} = {resultado}')