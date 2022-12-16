# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Seu peso (Kg): '))
altura = float(input('Sua altura (m): '))
imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está com ACIMA DO PESO!')
elif imc >= 30 and imc < 40:
    print('Você está OBESO!')
else:
    print('Você está com OBESIDADE MÓRBIDA!')
