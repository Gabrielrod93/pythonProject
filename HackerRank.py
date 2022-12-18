import ipdb
ipdb.set_trace()

alunos = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
notas = []
for v in alunos:
    notas.append(v[1])
notas.sort()
menor = min(notas)
while notas[0] == menor:
    notas.pop(0)
segunda = notas[0]
alunos.sort()
for i, v in enumerate(alunos):
    if alunos[i][1] == segunda:
        print(alunos[i][0])
