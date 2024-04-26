"""Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
consoantes"""

lista = []
consoantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
consoantesLidas = []

for i in range(10):
    caracter = input(f"Digite o {i + 1}º caractere: ").lower()
    lista.append(caracter)
    if caracter in consoantes:
        consoantesLidas.append(caracter)

totalConsoantes = len(consoantesLidas)
print(f"O total de consoantes é {totalConsoantes}")
print(f"As consoantes digitadas são: {consoantesLidas}")