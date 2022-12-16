# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

print('--- CADASTRO DE PESSOAS ---\n')
n_Pessoa = 1
mais_velho = homem = mulheres_menos_vinte = 0
while True:
    print(f'--- {n_Pessoa} ª PESSOA ---')
    n_Pessoa += 1
    # Variaveis
    idade = int(input('Idade: '))
    sexo = ' '
    # Lógica
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        mais_velho += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade <= 20:
        mulheres_menos_vinte += 1
    escolha = ' '
    while escolha not in 'SN':
        escolha = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print(f'Total de pessoas com mais de 18 anos {mais_velho}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulheres_menos_vinte} mulheres com menos de 20 anos')
