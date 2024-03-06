#  Funções para votação


def votar(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade >= 70 or idade in range(16, 18):
        return f'Com {idade} anos: VOTO OPCIONAL!'
    elif idade >= 18:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'
    else:
        return f'Com {idade} anos: NÃO VOTA!'


#  programa principal
print(votar(int(input('Qual ano você nasceu? '))))
