"""Faça um Programa que leia 4 notas, mostre as notas e a média na tela"""
notas = []
for i in range(4):
    nota = int(input(f"Digite a {i + 1}º nota: "))
    notas.append(nota)
    
avg = sum(notas) / 4
print(f"As notas são: {notas}")
print(f"A média das notas são: {avg:.1f}")
