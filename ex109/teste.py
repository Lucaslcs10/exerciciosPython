from ex109 import moeda

num = float(input("Digite um preço: R$"))
taxa = float(input("% de taxa: "))
print(f'A metade de {moeda.moeda(num)} é {(moeda.metade(num, True))}')
print(f'O dobro de {moeda.moeda(num)} é {(moeda.dobro(num, True))}')
print(f'Aumentando {moeda.moeda(num)} em {taxa}%, temos {(moeda.aumentar(num, taxa, True))}')
print(f'Diminuindo {moeda.moeda(num)} em {taxa}%, temos {(moeda.diminuir(num, taxa, True))}')
