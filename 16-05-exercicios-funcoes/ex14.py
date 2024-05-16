"""Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada
posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
lado 3, com números de 1 a 9:"""

import itertools

def quadrado_magico(perm):
    quadrado = [perm[:3], perm[3:6], perm[6:]]
    for linha in quadrado:
        if sum(linha) != 15:
            return False
    for col in range(3):
        if quadrado[0][col] + quadrado[1][col] + quadrado[2][col] != 15:
            return False
    if quadrado[0][0] + quadrado[1][1] + quadrado[2][2] != 15:
        return False
    if quadrado[0][2] + quadrado[1][1] + quadrado[2][0] != 15:
        return False
    return True
def encontra_quadrados_magicos():
    numeros = list(range(1, 10))
    quadrados_magicos = []
    for perm in itertools.permutations(numeros):
        if quadrado_magico(perm):
            quadrados_magicos.append(perm)
    return quadrados_magicos
def imprime_quadrado(quadrado):
    for i in range(3):
        print(quadrado[i*3:(i+1)*3])
    print()
quadrados_magicos = encontra_quadrados_magicos()
for quadrado in quadrados_magicos:
    imprime_quadrado(quadrado)


