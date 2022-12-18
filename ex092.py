cadastro = {}
cadastro['Nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
cadastro['idade'] = 2022-ano
cadastro['carteira'] = int(input('Carteira de trabalho: '))
if cadastro['carteira'] != 0:
    cadastro['ano'] = int(input('Ano de contratação: '))
    cadastro['salário'] = float(input('Salário: '))
    cadastro['Aposenta'] = (cadastro['ano']+35)-ano
for k, v in cadastro.items():
    print(f'{k} é igual {v}')
