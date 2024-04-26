"""Faça um Programa que leia um vetor de 5 números inteiros e mostre-os"""
def lerVetor():
    vetor = []
    print("Digite 5 números inteiros: ")
    for i in range(5):
        num = int(input(f"Digite o {i + 1}º número: "))
        vetor.append(num)
    return vetor

def mostrarNumeros(vetor):
    print("Números digitados: ")
    for num in vetor:
        print(num)

nums = lerVetor()
mostrarNumeros(nums)


