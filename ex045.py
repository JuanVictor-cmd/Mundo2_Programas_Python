# Crie um programa que faça o computador jogar Jokenpô com você.

# Bibliotecas
from random import randint
from time import sleep

# Opções de escolha
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

# Variáveis
jogador = int(input('Qual é a sua jogada? '))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

# JO KEN PO! com tempo de 1 segundo
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

# Resultado do Jogador e do Computador
print('-=' * 20)
print(f'O jogador jogou {itens[jogador]}')
print(f'O computador jogou {itens[computador]}')
print('-=' * 20)

# Condições if de escolhas
if computador == 0:  # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('JOGADOR PERDE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1:  # Computador jogou PAPEL
    if jogador == 0:
        print('JOGADOR PERDE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 2:  # Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('JOGADOR PERDE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
