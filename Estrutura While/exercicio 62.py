#Escreva um programa na tela que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementes de uma sequencai de fibnonnaci
print("Sequencia de Fibo")
print('= ' * 30)
n = int(input('Quantos termos você deseja mostrar ? '))
t1 = 0
t2 = 1
print(f'{t1} > {t2}', end ='')
c = 3

while c < n:
    t3 = t1 + t2
    print(f'> {t3}',end='')
    t1 = t2
    t2 = t3
    c += 1
print("> Fim")