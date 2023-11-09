#desenvolva uma logica que leia o peso e a altura da pessoa, calcule o imc e de acordo com isso mostre seu status, de acordo com a tabela abaixo:
# abaixo de 18.5 - abaixo do peso
# entre 18.5 e 25 peso ideal
# entre 25 até 30 - sobrepeso
# entre 30 até 30 obesidade
# acima de 40 - obesidade

altura = float(input("Digite sua altura: "))

peso  = float( input("digite seu peso "))

IMC = peso / (altura  * altura)

IMC_arredondado = round(IMC, 2)

print(IMC_arredondado)

if IMC < 18:
    print('abaixo do peso')
elif 18.5 <= IMC < 24.9:
    print("peso ideal")
elif 25 <= IMC < 30:
    print('sobrepeso')
elif 30 <= IMC < 39.9:
    print('obesidade')
else:
    print('obesidade agressiva')
    