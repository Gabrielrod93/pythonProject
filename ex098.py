def contagem(i, f, p):
    print('-='*30)
    print(f'Contagem de {i} até {f} de {p} em {p}:')
    for c in range(i, f, p):
        print(c, end = ' ')
    print()
    print('-='*30)

contagem(1, 10, 1)
contagem(10, 0, -2)
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contagem(inicio, fim, passo)