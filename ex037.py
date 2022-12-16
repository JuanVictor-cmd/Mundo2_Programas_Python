# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('Escolha qual será a base de conversão:')
print('[1] Binário\n[2]Octal\n[3]Hexadecimal')
escolha = int(input('Sua escolha: '))

if escolha == 1:
    print(f'{num} convertido para BINÁRIO é {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é {hex(num)[2:]}')
else:
    print('Opção inválida!')
