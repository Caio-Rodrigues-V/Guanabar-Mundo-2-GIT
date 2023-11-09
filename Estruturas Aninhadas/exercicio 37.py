"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuario escolher qual será a base de conversão:
1 - para binario
2 - para octal
3 - hexadecimal
"""

numero = int(input("Digite um numero que queira converteR? "))

print("Escolha a base de conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")

opcao = int(input("Digite para oque deseja converter: "))

if opcao == 1:
    resultado = bin(numero)
    print(f"O numero {numero} em binario é {resultado}")
elif opcao == 2:
    resultado = oct(numero)
    print(f"O numero {numero} em binario é {resultado}")
elif opcao == 3:
    resultado = hex(numero)
    print(f"O numero {numero} em binario é {resultado}")
else:
    print('opcao invalida')
