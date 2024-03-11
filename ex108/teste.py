from ex108 import moeda

num = float(input("Digite um preço: R$"))
taxa = int(input("% de taxa: "))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando {moeda.moeda(num)} em {taxa}%, temos {moeda.moeda(moeda.aumentar(num, taxa))}')
print(f'Diminuindo {moeda.moeda(num)} em {taxa}%, temos {moeda.moeda(moeda.diminuir(num, taxa))}')
