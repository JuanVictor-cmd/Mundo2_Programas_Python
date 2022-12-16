# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do
# homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
homem_velho = ''
idade_mulher = 0
for pessoa in range(1, 5):
    print(f'----- {pessoa}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    if pessoa == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_velho = nome
    else:
        if sexo in 'Mm' and idade > maior_idade_homem:
            maior_idade_homem = idade
            homem_velho = nome
    if sexo in 'Ff' and idade <= 20:
        idade_mulher += 1
soma_idade += idade
media_idade = soma_idade / 2
print(f'A média de idade do grupo é de {media_idade}')
print(
    f'O homem mais velho tem {maior_idade_homem} anos e se chama {homem_velho}')
print(f'Ao todo são {idade_mulher} mulheres com menos de 20')
