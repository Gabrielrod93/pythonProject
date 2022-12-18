jogador = {}
gol = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for v in range(0, partidas):
    gols = int(input(f'Quantos gols fez na {v}a partida? '))
    gol.append(gols)
    jogador['gol'] = gol
    total = total+gols
jogador['total'] = total
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for i, v, in enumerate(gol):
    print(f'Na partida {i} ele fez {v} gols')