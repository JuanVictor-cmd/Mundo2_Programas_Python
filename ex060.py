# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('Digite um número para\ncalcular seu Fatorial: '))

fatorial = 1
cont = num

print(f'Calculando {num}! = ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(f' x ' if cont > 1 else ' = ', end='')
    fatorial *= cont
    cont -= 1
print(f'{fatorial}')
