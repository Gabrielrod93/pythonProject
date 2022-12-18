def notas(*list, sit=False):
    tudo = {}
    tudo['Total'] = len(list)
    tudo['Maior'] = max(list)
    tudo['Menor'] = min(list)
    media = sum(list)/len(list)
    tudo['Média'] = media
    if sit:
        if media <= 6:
            tudo['Situação'] = 'Ruim'
        if media > 7:
            tudo['Situação'] = 'Boa'
    return tudo


resp = notas(5, 3, 7, 2, 10, sit=True)
print(resp)