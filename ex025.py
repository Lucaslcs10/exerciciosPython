print('Procurando uma string dentro de outra')
nome = input('Qual é o seu nome? ').strip().title()
print(f'O seu nome tem Silva?', end=" ")
if 'Silva ' in nome + ' ':
    print('Sim!')
else:
    print('Não!')
