# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele
# conquistou no final do jogo.
from random import randint
# Introdução
cont = 0
v = 0
while cont < 2:
    print('-'*20)
    print('VAMOS JOGAR PAR OU ÍMPAR!')
    print('-'*20)
# Variáveis
    jogador = int(input('Digite um número: '))
    computador = randint(1, 11)
    condicao = ' '
    while condicao not in 'PpIi':
        condicao = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    total = jogador + computador
    cont += 1
    print('-'*20)
# Condicionais
    if condicao == 'P':  # Par
        if total % 2 == 0:
            print(
                f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU PAR!')
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
    elif condicao == 'I':  # Impar
        if total % 2 != 0:
            print(
                f'Você jogou {jogador} e o computador {computador}. Total de {total} DEU ÍMPAR!')
            print('VOCÊ GANHOU!')
            v += 1
        else:
            print('VOCÊ PERDEU!')
print(f'GAMEOVER! Você venceu {v} vezes!')
