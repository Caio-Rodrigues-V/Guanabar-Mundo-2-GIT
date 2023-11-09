#faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade:
# 1- se ele ainda vai se alistar ao serviço militar
# 2- se é a hora de se alistar
# 3- se ja passou da hora de se alistar
#seu progama tbm deve mostar quanto tempo falta para o prazo ou se ja passou

ano = int(input('em que ano você nasceu? '))

alistamento = 2023 - ano

if alistamento > 18:
    print('voce ja passou da hora de se alistar')
    tempo =  alistamento - 18
    print(f'ja se passaram {tempo} que voce ja se alistou')
elif alistamento < 18:
    tempo =  18 - alistamento
    print(f'ainda faltam {tempo} anos para você se alistar ! ')
elif alistamento == 18:
    print("hora perfeita de se alistar aos serviços militar ")