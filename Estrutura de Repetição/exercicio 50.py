soma = 0
cont = 0
for i in range(1,7):
    num = int(input("Digite um valor: "))
    if num % 2 == 0:
        soma += num
        cont = +1 
print("Esse é o total de todos os numeros pares digitados",soma)