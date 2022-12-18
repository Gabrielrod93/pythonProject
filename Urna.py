Ciro = 0
Lula = 0
Bolsonaro = 0
nulo = 0
candidatos = [Ciro, Lula, Bolsonaro]
seção = ['Claudia', 'Bi', 'Joao', 'Marcia', 'Safira', 'Enzo']
while len(seção) != 0:
    nome = str(input('Digite seu nome: '))
    while nome not in seção:
        nome = str(input('Nome não encontrado, digite outro nome: '))
    while True:
        voto = int(input('Digite seu voto (00 para nulo): '))
        if voto == 00:
            nulo = nulo + 1
        if voto == 13:
            Lula = Lula + 1
        if voto == 22:
            Bolsonaro = Bolsonaro + 1
        if voto == 30:
            Ciro = Ciro + 1
        seção.remove(nome)
        break

print(f'O candidato vencedor foi {max(candidatos)}')
