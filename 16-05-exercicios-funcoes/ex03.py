"""Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três
argumentos"""


def soma_tres(a, b, c):
    return a + b + c
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))
resultado = soma_tres(num1, num2, num3)
print("A soma dos três números é:", resultado)