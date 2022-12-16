# Melhore o jogo do DESAFIO 28 onde o computador vai
# “pensar” em um número entre 0 e 10. Só que agora o
# jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
computador = randint(0, 10)
print('-'*20)
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar qual foi?')
print('-'*20)
numero = int(input('Qual seu palpite? '))
tentativas = 1
while numero != computador:
    if numero > computador:
        print('Menos...Tente mais uma vez')
        numero = int(input('Qual seu palpite? '))
        tentativas += 1
    else:
        print('Mais...Tente mais uma vez')
        numero = int(input('Qual seu palpite? '))
        tentativas += 1
if numero == computador:
    print(f'PARABÉNS!! o número que pensei foi {computador}!')
    print(f'Você acertou com {tentativas} tentativas!')
else:
    print(f'ERROU! o número que pensei foi {computador} e não {numero}!')
