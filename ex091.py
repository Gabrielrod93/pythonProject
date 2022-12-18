import random
from operator import itemgetter
resultados = {}
ranking = {}
for i in range(1, 5):
    n = random.randrange(1, 6)
    print(f'jogador {i} tirou {n}')
    resultados[f'jogador {i}'] = n
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'{k+1}o lugar: {v[0]} tirou {v[1]}')