# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.
print('-' * 20)
num = int(input('Digite o número da tabuada: '))
for x in range(11):
    mul = num * x
    print(f'{num} X {x} = {mul}')
print('-' * 20)
