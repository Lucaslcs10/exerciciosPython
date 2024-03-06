print('Índice de Massa Corporal')
peso = float(input('Qual é o seu peso em Kg? '))
altura = float(input('Qual a sua altura? '))
if altura.is_integer():
    altura = altura / 100
imc = peso / (altura * altura)
if imc <= 18.5:
    print(f'IMC de {imc:.1f} Abaixo do peso!')
elif imc <= 25:
    print(f'IMC de {imc:.1f} Peso ideal!')
elif imc <= 30:
    print(f' IMC de {imc:.1f} Sobrepeso!')
elif imc <= 40:
    print(f'IMC de {imc:.1f} Obesidade!')
else:
    print(f'IMC de {imc:.1f} Obesidade mórbida!')
