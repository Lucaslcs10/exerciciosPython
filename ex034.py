print('Aumentos múltiplos')
sa = float(input('Qual o salário atual? R$'))
if sa <= 1250:
    print(f'O salário atual de R${sa:.2f} com aumento de 15% passa a ser de R${sa * 1.15:.2f}')
else:
    print(f'O salário atual de R${sa:.2f} com aumento de 10% passa a ser de R${sa * 1.10:.2f}')
print(' ')
print('FIM')
