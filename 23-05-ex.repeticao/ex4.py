#Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
#crescente.

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
n4 = float(input("Digite o quarto número: "))
n5 = float(input("Digite o quinto número: "))

while True:
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n3 > n4:
        n3, n4 = n4, n3
    if n4 > n5:
        n4, n5 = n5, n4

    if n1 <= n2 <= n3 <= n4 <= n5:
        break

print("Números em ordem crescente:", n1, n2, n3, n4, n5)
