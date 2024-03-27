print("Vamos calcular as raízes de uma equação do 2º grau!")
A = int(input("Digite o valor para A: "))
B = int(input("Digite o valor para B: "))
C = int(input("Digite o valor para C: "))

# primeira raiz
raiz1 = (-B + (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
raiz2 = (-B - (B ** 2 - 4 * A * C) ** 0.5) / (2 * A)
print(f"As raízes da sua equação serão: x1: {raiz1:.0f} e x2: {raiz2:.0f}")






