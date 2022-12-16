# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print('--- LOJA SUPER BARATÃO ---\n')
total = menor = cont = mais_mil = 0
barato = ' '
while True:
    produto = input('Nome do Produto: ')
    preço = float(input('Preço: '))
    cont += 1
    total += preço
    if preço > 1000:
        mais_mil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar? [S/N] ').strip().upper()[0]

    if escolha == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {mais_mil} produtos custando mais de R$1.000')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')
