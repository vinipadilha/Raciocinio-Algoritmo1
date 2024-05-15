"""A matriz identidade é uma matriz de mesma quantidade de linhas e
colunas que tem todos os elementos da diagonal principal (de cima para
baixo, esquerda para direita) iguais a 1, e demais elementos iguais a 0.
Criar um programa que solicita o tamanho da matriz desejada, que gera a
matriz identidade."""

size = int(input("Digite o tamanho da matriz desejada: "))

def matrizIdentidade(size):
    matriz = []
    for i in range(size):
        linha = []
        for x in range(size):
            if i == x:
                linha.append(1)
            else:
                linha.append(0)     
        matriz.append(linha)
    return matriz

matrizID = matrizIdentidade(size)

for linha in matrizID:
    print(linha)