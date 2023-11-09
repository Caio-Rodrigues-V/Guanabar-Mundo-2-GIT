#Desenvolva um programa que leia o primeiro termo de uma PA e a razão de uma PA, no final mostre os 10 primeiros termos dessa progressao
razao = int(input("Digite a razão da PA: "))
Prim_Termo = int(input("Digite o primeiro termo: "))
decimo = Prim_Termo + (10 - 1 ) * razao
for i in range(Prim_Termo,decimo + razao ,razao):
    print(f"{i}", end = ' > ')
    
