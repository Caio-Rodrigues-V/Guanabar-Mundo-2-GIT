#refaça o desafio 035 dos triangulos e acrescente o recurso de mostrar o tipo do triangulo
# quilatero : todos os lados iguais
# isosceles : dois lados iguais
# escaleno: todos os lados diferentes

# Solicita ao usuário que insira o comprimento das três retas
a = float(input("Digite o comprimento da primeira reta: "))
b = float(input("Digite o comprimento da segunda reta: "))
c = float(input("Digite o comprimento da terceira reta: "))

# Verifica se as retas podem formar um triângulo
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Forma um triangulo equilatero: todos os lados sao iguais')
    elif a==b or a == c or b == c:
        print('Forma um triangulo isosceles: dois lados iguis ')
    else:
        print('forma um triangulo escaleno: todos lados diferentes')
else:
    print('nao formam triangulo')