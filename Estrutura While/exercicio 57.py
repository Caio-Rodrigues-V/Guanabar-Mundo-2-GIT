#faça um programa que leia o sexo de uma pessao, mas só aceite os valors 'm' ou 'f'.
#caso esteja errado, peça a digitação novamente ate ter um valor correto

sexo = input("Digite seu sexo [M/F] ").lower().strip()[0]
while sexo not in 'mf':
    sexo = str(input("Dados invalidos, digite seu sexo: ")).lower().strip()[0]
print(f'sexo {sexo} registrado com sucesso')