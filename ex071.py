# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

print('--- Banco do Juan ---')

valor = int(input('Qual valor você quer sacar? R$'))
total = valor
céd = 50
total_ced = 0
while True:
    if total >= céd:
        total -= céd
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        total_ced = 0
        if total == 0:
            break
print('Volte sempre!')
