from datetime import date
print('Alistamento Militar')
print('[ 1 ] MASCULINO')
print('[ 2 ] FEMININO')
se = int(input('Qual seu gênero? '))
if se == 2:
    print('Você não precisa se alistar!')
    breakpoint()
idade = int(input('Qual ano você nasceu? '))
idadef = date.today().year - idade
if idadef == 18:
    print(f'Você tem {idadef} anos e deve se alistar imediatamente!')
elif idadef == 17:
    print(f'Você tem {idadef} anos e deve se alistar ano que vem!')
elif idadef < 17:
    print(f'Você tem {idadef} anos e deve se alistar em {18 - idadef} anos!')
elif idadef == 19:
    print(f'Você tem {idadef} anos e deveria ter se alistado ano passado!')
else:
    print(f'Você tem {idadef} anos.')
    print(f'e deveria ter se alistado em {date.today().year - (idadef - 18)} há {idadef - 18} anos!')
