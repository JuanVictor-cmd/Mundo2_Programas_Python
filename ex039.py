# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do
# tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você precisa se alistar IMEDIATAMENTE!')
elif idade < 18:
    anos = 18 - idade
    print(
        f'Você ainda não tem 18 anos. Ainda faltam {anos} anos para seu alistamento!')
    print(f'Seu alistamento será em {anos + atual}')
elif idade > 18:
    anos = idade - 18
    print(f'Você já deveria ter se alistado há {anos} anos')
    print(f'Seu alistamento foi em {atual - anos}')
