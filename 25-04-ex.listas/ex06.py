"""Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
imprima o número de alunos com média maior ou igual a 7.0"""

mediaAlunos = []
for aluno in range(10):
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a {i + 1}º nota do aluno {aluno + 1}: "))
        notas.append(nota)
    avg = sum(notas) / len(notas)
    mediaAlunos.append(avg)

maior7 = 0

for media in mediaAlunos:
    if media >= 7:
        maior7 += 1

print(f"{maior7} alunos tiverem média maior ou igual a 7")
