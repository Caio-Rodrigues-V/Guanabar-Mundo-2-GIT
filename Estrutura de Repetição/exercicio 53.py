#Crie um programa que leia a frase qualquer e diga se ela é um palindromo, desconsiderando so espaços

frase = str(input("Que frase deseja inverter? ")).strip()
frase_revertida = ''

for letra in reversed(frase):
    frase_revertida +=letra

if frase_revertida == frase:
    print(frase_revertida)
    print('é um palindromo')
    
else:
    print(frase_revertida)
    print('NAOé um palindromo! ')
