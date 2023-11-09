#Crie um programa que leia dois valors e mostre o menu como ao lado da tela:
#Seu programa deverá realizar a opração solicitada




while True:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    print('[1] Soma')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão' )

    escolha = input("Digite uma opção 1. 2. 3. 4. ")

    if escolha == '1':
        resultado = numero1 + numero2
        print(f'o resultado da soma do numero 1 e numero 2 é de {resultado}')
    
    elif escolha == '2':
        resultado = numero1 - numero2
        print(f'o resultado da subtração entre os 2 numeros foi é de : {resultado}')
    
    elif escolha == '3':
        resultado = numero1 * numero2
        print(f'O resultado da multiplicação é de {resultado}')
    
    elif escolha == '4':
        resultado = numero1 / numero2
        print(f'o resultado da divisão entre os 2 numeros é de {resultado}')
    else:
        print("Opção invalida")
    continuar = input("Deseja continuar? [S/N]").upper()
    if continuar != 'S':
        print('operações pausadas')
        break    