#  Analisando e gerando Dicionários


def notas(*n, sit):
    """
    ->Analisa notas e situações de vários alunos.
    :param n: Notas dos alunos (aceita várias).
    :param sit: Opcional, mostra a situação do aluno.
    :return: Dicionário com informações da turma de alunos.
    """
    lista = {}  # cria um dicionário
    lista['total'] = len(n)  # cria (key) 'total' e atribui (value) = total de notas(n)
    lista['maior'] = max(n)  # cria (key) 'maior' e atribui (value) = maior de notas(n)
    lista['menor'] = min(n)  # cria (key) 'menor' e atribui (value) = menor de notas(n)
    lista['média'] = round(sum(n) / len(n), 2)  # cria (key) 'média' e atribui (value) = soma de (n) / total de (n)

    if sit:  # se (sit) = True
        if lista['média'] >= 7:  # se ['média'] em {lista} >= 7 ↓
            lista['situação'] = 'BOA!'
        elif lista['média'] >= 6:  # se ['média'] em {lista} >= 6 ↓
            lista['situação'] = 'RAZOÁVEL!'
        else:  # se não ↓
            lista['situação'] = 'RUIM!'

    return lista


#  programa principal
resp = notas(5.9, sit=True)
print(resp)
