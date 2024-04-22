"""Criar um programa que efetua a soma de duas matrizes 3x3, sabendo
que a soma das matrizes 3x3 é uma nova matriz 3x3 onde cada elemento
é resultado da soma dos elementos das matrizes na mesma posição"""
"""
matriz1 = [
    [1, 4, 7], 
    [2, 5, 8], 
    [3, 6, 9]
    ]
"""
def somar(matriz1, matriz2):
    somaMatriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):
        for x in range(3):
            somaMatriz[i][x] = matriz1[i][x] + matriz2[i][x]

    return somaMatriz

def ler(matriz):
     for y in matriz:
        print(y)

matriz1 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
matriz2 = [[3, 2, 3], [1, 3, 3], [0, 2, 2]]

resultadoSoma = somar(matriz1, matriz2)
print("Matriz resultante da soma das matrizes:")
ler(resultadoSoma)
