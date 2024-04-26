"""Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa."""
vetor = []
print("Digite 10 números inteiros: ")
for i in range(10):
    num = int(input(f"Digite o {i + 1}º número: "))
    vetor.append(num)

vetor.reverse() 
print(f"Lista invertida: {vetor}")

