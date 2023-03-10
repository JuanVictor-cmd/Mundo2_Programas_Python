# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço normal
# – 3x ou mais no cartão: 20% de juros
print('-' * 20)
print('Loja Guanabara')
print('-' * 20)
compras = float(input('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] à vista dinheiro/cheque
[2] à vista no cartão'
[3] em até 2x no cartão'
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    desconto = compras - (compras * 10 / 100)
    print(
        f'Sua compra de R${compras:.2f} vai custar R${desconto:.2f} no final.')
elif opcao == 2:
    desconto = compras - (compras * 5 / 100)
    print(
        f'Sua compra de R${compras:.2f} vai custar R${desconto:.2f} no final.')
elif opcao == 3:
    parcela = compras / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opcao == 4:
    total = compras + (compras * 20 / 100)
    parcelas = int(input('Quantas parcelas? '))
    toparcelas = total / parcelas
    print(
        f'Sua compra será parcelada em {parcelas}x de R${toparcelas:.2f} COM JUROS')
else:
    print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE :)')
