"""A matriz identidade é uma matriz de mesma quantidade de linhas e
colunas que tem todos os elementos da diagonal principal (de cima para
baixo, esquerda para direita) iguais a 1, e demais elementos iguais a 0.
Criar um programa que solicita o tamanho da matriz desejada, que gera a
matriz identidade."""

size = int(input("Digite o tamanho da matriz desejada: "))

def matrizIdentidade(tamanho):
    matriz = []
    for i in range(tamanho):
        linha = []
        for x in range(tamanho):
            if i == x:
                linha.append(1)
            else:
                linha.append(0)     
    return matriz

def printarMatriz(matriz):
    for y in matriz: