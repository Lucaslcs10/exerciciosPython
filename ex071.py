#  Simulador de Caixa Eletrônico
print('='*25)
print(f'{"BANCO DO POVO - BDP":>22}')
print('='*25)
saque = int(input('Qual o valor do saque? R$'))
total = saque
ce = 50
co = 0
while True:
    if total >= ce:
        total = total - ce
        co = co + 1
    else:
        if co > 0:
            print(f'{co} Cédulas de R${ce} sacada(s)')
        if ce == 50:
            ce = 20
        elif ce == 20:
            ce = 10
        elif ce == 10:
            ce = 1
        co = 0
        if total == 0:
            break
print('-'*21)
print('Finalizando operação')
print('-'*21)
