# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

if num > num2:
    print('O PRIMEIRO valor é maior!')
elif num2 > num:
    print('O SEGUNDO valor é maior!')
elif num == num2:
    print('Ambos valores são IGUAIS!')
