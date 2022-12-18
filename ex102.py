def fatorial(a, show=False):
    f = 1
    for v in range(a, 0, -1):
        f = f*v
        if show:
            print(v, end = ' ')
    return f


print(f'O fatorial é {fatorial(5, show=True)}')