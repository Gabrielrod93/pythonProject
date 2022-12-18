dados = {}
nome = str(input('Nome: '))
media = float(input('Média: '))
dados['nome'] = nome
dados['media'] = media
if media < 7:
    dados['situação'] = 'reprovado'
else:
    dados['situação'] = 'aprovado'
for i, k in dados.items():
    print(f'{i} é igual {k}')
