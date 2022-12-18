def voto(ano):
    if 16 <= 2022-ano < 18 or 2022-ano >= 65:
        return 'Opcional'
    if 2022-ano >= 18:
        return 'Obrigatorio'
    if 2022-ano < 16:
        return 'Negado'

ano = int(input('Qual ano de nascimento? '))
print(f'Seu voto é {voto(ano)}')