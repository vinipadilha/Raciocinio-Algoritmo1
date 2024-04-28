"""Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
elementos do vetor"""
vetor = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número(inteiro): "))
    vetor.append(num)

soma = 0
for num in vetor:
    soma += num**2
    
print(f"A soma dos quadrados dos elementos é: {soma}")
