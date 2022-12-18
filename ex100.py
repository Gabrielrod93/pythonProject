import random
def sorteia(lista):
    for contador in range(0, 5):
        lista.append(random.randint(1, 10))


def somapar(lista):
    soma = 0
    for c in lista:
        if c %2 == 0:
            soma = soma+c
    print(soma)

numeros = []
sorteia(numeros)
print(numeros)
somapar(numeros)