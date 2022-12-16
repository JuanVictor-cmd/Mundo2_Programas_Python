# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.


option = 1
while option != 0:
    print('-' * 20)
    print('10 TERMOS DE UMA PA')
    print('-' * 20)
    primeiro = int(input('Primeiro Termo: '))
    razao = int(input('Razão: '))
    termo = primeiro
    cont = 1
    while cont <= 10:
        print(f'{termo} → ', end='')
        termo += razao
        cont += 1
    print('FIM')
    print('[ 1 ] Mostrar mais termos ')
    print('[ 0 ] Sair ')
    option = int(input('Qual sua opção? '))
    if option == 1:
        continue
    elif option == 0:
        print('FIM')
        break
