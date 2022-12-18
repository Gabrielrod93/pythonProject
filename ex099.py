def maior(*num):
    print('Analisndo os valores...')
    print(num)
    print(f'Foram passados {len(num)} valores ao todo')
    maior = menor = 0
    for i, v in enumerate(num):
        if i == 0:
            maior = menor = v
        elif menor > v:
            menor = v
        elif maior < v:
            maior = v
        print(v, end = ' ')
    print(f'O maior valor é {maior}')



maior(5, 2, 6)