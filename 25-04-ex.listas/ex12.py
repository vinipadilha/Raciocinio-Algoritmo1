"""Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
13 anos possuem altura inferior à média de altura desses alunos."""
alunos = 30  
idades = []
alturas = []

for i in range(alunos):
    ida = int(input(f"Digite a idade do {i + 1}º aluno: "))
    alt = float(input(f"Digite a altura do {i + 1}º aluno: "))
    idades.append(ida)
    alturas.append(alt)

totalAlunos = 0
somaAlturas = 0
abaixoMedia = 0

for i in range(alunos):
    if idades[i] > 13:
        somaAlturas += alturas[i]
        totalAlunos += 1

avg = somaAlturas / totalAlunos

for i in range(alunos):
    if idades[i] > 13 and alturas[i] < avg:
        abaixoMedia += 1

print(f"A quantidade de alunos com mais de 13 anos e abaixo da média de altura desses mesmos são: {abaixoMedia}")
    
    




    
        
