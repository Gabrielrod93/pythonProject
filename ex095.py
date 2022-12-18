jogador = {}
gol = []
total = 0
resp = ' '
time = []
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for v in range(0, partidas):
        gols = int(input(f'Quantos gols fez na {v}a partida? '))
        gol.append(gols)
        jogador['gol'] = gol[:]
        total = total+gols
    jogador['total'] = total
    time.append(jogador.copy())
    gol.clear()
    jogador.clear()
    resp = str(input('Quer continuar? ')).strip().upper()[0]
    if resp in 'N':
        break
print('-='*30)
print(f'Cod', f'{"Nome":^10}', f'{"gols":^15}', f'{"total":>5}')
for i, v in enumerate(time):
    print(i, end = '')
    print(f'{time[i]["nome"]:^15}', end = '')
    print(f'{time[i]["gol"]}', end = '')
    print(f'{time[i]["total"]:>15}')
while True:
    resp = int(input('Quer mostrar os dados de qual jogador? (999 para encerrar): '))
    if resp == 999:
        break
    else:
        print(f'Levantamento do jogador {time[resp]["nome"]}')
        for i, v in enumerate(time[resp]['gol']):
            print(f'No jogo {i} ele fez {v}')

