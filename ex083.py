#  Validando expressões matemáticas
expre = input('Digite sua expressão: ')
lista = []
for c in expre:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append('error')
            break
if len(lista) == 0:
    print('Sua expressão é válida!')
else:
    print('Sua expressão não é válida!')
