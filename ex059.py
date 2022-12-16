# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))

option = 0
while option != 5:
    print('-'*20)
    print('[ 1 ] somar ')
    print('[ 2 ] multiplicar ')
    print('[ 3 ] maior ')
    print('[ 4 ] novos números ')
    print('[ 5 ] sair do programa ')
    option = int(input('>>>>>>>> Qual sua opção? '))
    print('-'*20)
    if option == 1:
        print(f'A soma de {n1} e {n2} é igual a {n1+n2:.2f}')
    elif option == 2:
        print(f'A multiplicação de {n1} e {n2} é igual a {n1*n2:.2f}')
    elif option == 3:
        maior = max(n1, n2)
        print(f'O maior valor é: {maior}')
    elif option == 4:
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif option == 5:
        break

print('Fim do programa, volte sempre!')
