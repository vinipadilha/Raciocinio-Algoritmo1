"""Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
PAR e os números IMPARES no vetor impar. Imprima os três vetores"""
nums = []
for i in range(20):
    num = int(input(f"Digite o {i + 1}º número: "))
    nums.append(num)

numsP = []
numsI = []

for i in nums:
    if i % 2 == 0:
        numsP.append(i)
    else:
        numsI.append(i)

print("Aqui está a lista de todos os números:")
print(nums)
print("========================================")
print("Aqui está a lista dos números pares:")
print(numsP)
print("========================================")
print("Aqui está a lista dos números ímpares:")
print(numsI)
print("========================================")
