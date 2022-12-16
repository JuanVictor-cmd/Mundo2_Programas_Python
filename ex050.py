# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for x in range(0, 6):
    inteiro = int(input('Digite seis números inteiros: '))
    if inteiro % 2 == 0:
        soma = soma + inteiro
        cont = cont + 1
print(
    f'Você informou {cont} números PARES e a soma dos valores PARES é: {soma}')
