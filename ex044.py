print('Gerenciador de Pagamentos')
compra = float(input('Qual o preço das compras? R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] À VISTA DINHEIRO/CHEQUE')
print('[ 2 ] À VISTA CARTÃO')
print('[ 3 ] 2x NO CARTÃO')
print('[ 4 ] 3x OU MAIS NO CARTÃO')
op = int(input('Qual a opção? '))
if op == 1:
    print(f'Pagando à vista você tem desconto de 10%')
    print(f'Com o desconto a sua compra de R${compra:.2f} fica em R${compra - (compra * 10 / 100):.2f}')
elif op == 2:
    print(f'Pagando à vista no cartão você tem desconto de 5%')
    print(f'Com o desconto a sua compra de R${compra:.2f} fica em R${compra - (compra * 5 / 100):.2f}')
elif op == 3:
    print(f'Pagando em até 2x no cartão sem juros')
    print(f'A sua compra fica no valor de 2 parcelas de R${compra / 2:.2f}')
elif op == 4:
    print(f'Pagando em 3x ou mais no cartão você tem um juros de 20%')
    print(f'A sua compra de R${compra} fica no valor de {compra + (compra * 20 / 100)}')
else:
    print('Opção inválida!')
    