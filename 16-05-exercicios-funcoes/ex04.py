"""Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere 'P', se
seu argumento for positivo, e 'N', se seu argumento for zero ou negativo."""

def verificar_sinal(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'
num = float(input("Digite um número: "))
resultado = verificar_sinal(num)
print("O resultado é:", resultado)


