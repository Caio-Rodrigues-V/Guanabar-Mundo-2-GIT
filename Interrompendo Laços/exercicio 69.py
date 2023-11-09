sexoM = 0
mulhermenos20 = 0
maiorde18 = 0

while True:
    sexo = input("Digite seu Sexo: [M/F] ").strip().lower()
    idade = int(input("Digite sua idade: "))

    if idade > 18:
        maiorde18 += 1
        print("Você tem mais de 18 anos")

    if sexo == "m":
        sexoM += 1
        print("Mais um homem cadastrado!")

    if sexo == "f" and idade < 20:
        mulhermenos20 += 1
        print("Mais uma mulher com menos de 20 anos registrada!")

    continuar = input("Deseja continuar? [S/N] ").strip().lower()
    if continuar != "s":
        break

print(f"Total de pessoas maiores de 18 anos: {maiorde18}")
print(f"Total de homens cadastrados: {sexoM}")
print(f"Total de mulheres com menos de 20 anos: {mulhermenos20}")
