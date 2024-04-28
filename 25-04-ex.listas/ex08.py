"""Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida."""

registros = []

for i in range(5):
    idade = float(input(f"Digite a idade da {i + 1}º pessoa. Ex(23): "))
    altura = float(input(f"Digite a altura da {i + 1}º pessoa. Ex(1.73): "))
    pessoa = [idade, altura]
    registros.append(pessoa)

print("Idade e altura na ordem inversa: ")
for pessoa in reversed(registros):
    print(f"Idade: {pessoa[0]}, Altura: {pessoa[1]}")
    