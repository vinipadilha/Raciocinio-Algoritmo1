"""Dado o vetor nums = [3, 7, 2, 9, 5, 6] criar um programa que, em
uma linha, calcula a média dos seus elementos"""

nums = [3, 7, 2, 9, 5, 6]

soma = sum(nums)
quant = len(nums)
media = soma / quant
print(f"A média é: {media:.2f}")
