def boletim(*n, sit=False):
    r = dict()
    r['Total'] = len(n)
    r['Menor'] = min(n)
    r['Maior'] = max(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] > 6:
            r['Situação'] = 'Aprovado'
        elif r['Média'] <= 6:
            r['Situação'] = 'Recuperação'
        else:
            r['Situação'] = 'Reprovado'
    return r


resp = boletim(5.5, 7, 8, 4, sit=True)
print(resp)
