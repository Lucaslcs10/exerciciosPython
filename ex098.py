from time import sleep
#  Função de Contador


def contador(i, f, p):
    cont = i
    if p == 0:
        p = 1
        print('Passo 0 = 1')
    print('-' * 40)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    sleep(1)
    if i < f:
        while cont <= f:
            print(cont, end=' ')
            sleep(0.3)
            cont = cont + p
        sleep(0.3)
        print('FIM!')
    else:
        while cont >= f:
            print(cont, end=' ')
            sleep(0.3)
            cont = cont - p
        sleep(0.3)
        print('FIM!')


#  programa principal
contador(1, 10, 1)
sleep(1)
contador(10, 0, 2)
print('-' * 40)
print('Agora é com você!')
contador(int(input('Início: ')), int(input('Fim: ')), (abs(int(input('Passo: ')))))
