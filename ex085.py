#  Listas com pares e ímpares
todos = [[], []]
for c in range(1, 8):
    v = int(input(f'Digite o {c}º valor: '))
    if v % 2 == 0:
        todos[0].append(v)
    else:
        todos[1].append(v)
print('* '*30)
print(f'Valores pares digitados: {sorted(todos[0])}')
print(f'Valores ímpares digitados: {sorted(todos[1])}')
