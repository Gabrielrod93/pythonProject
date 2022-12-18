pessoa = {}
todos = []
resp = ' '
media = soma = 0
while True:
    nome = str(input('Nome: '))
    pessoa['nome'] = nome
    idade = int(input('Idade: '))
    soma = soma+idade
    pessoa['idade'] = idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    while sexo not in 'MF':
        print('Erro')
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    pessoa['sexo'] = sexo
    todos.append(pessoa.copy())
    pessoa.clear()
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    while resp not in 'SN':
        print('Erro!')
        resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp in 'N':
        break
media = soma/(len(todos))
print('-='*30)
print(f'Foram cadastradas {len(todos)} pessoas')
print(f'A média de idade é de {media}')
print('As mulheres cadastradas foram ', end = '')
for i, v in enumerate(todos):
    if todos[i]['sexo'] == 'F':
        print(todos[i]['nome'], end = ', ')
print()
print('Temos acima da média', end = ' ')
for i, v in enumerate(todos):
    if todos[i]['idade'] > media:
        print(todos[i]['nome'], end = ', ')
