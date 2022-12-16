# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('--- Programa da Tabuada ---')
print('Digite um número negativo para parar o programa.')

while True:
    num = int(input('Digite o valor da tabuada: '))
    if num < 0:
        break
    print(f'--- Tabuada de {num} ---')
    for x in range(1, 11):
        print(f'{num} x {x} = {num*x}')
print('FIM')
