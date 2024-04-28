"""Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números"""
nums = []
for i in range(5):
    num = float(input(f"Digite o {i + 1}º número: "))
    nums.append(num)

soma = sum(nums)
multi = 1

for num in nums:
    multi *= num

print(f"Números digitados: {nums}")
print(f"Soma dos números: {soma:.0f}")
print(f"Multiplicação dos números: {multi:.0f}")