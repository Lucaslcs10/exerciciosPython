s = ''
while s != 'M' and s != 'F':
    s = input('Qua l o seu sexo? [M/F] ').upper().strip()
    if s != 'M' and s != 'F':
        print('Opção inválida. Tente novamente!')
print('Opção registrada. Obrigado!')
