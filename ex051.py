# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.


print('-' * 20)
print('10 TERMOS DE UMA PA')
print('-' * 20)

termo = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
decimo = termo + 10 * razao
for i in range(termo, decimo, razao):
    print(f'{i}', end=' -> ')
print('ACABOU')
