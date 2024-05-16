"""Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado"""
def contarDigitos(num):
    return len(str(num))


num = int(input("Digite um número inteiro: "))

qntDigitos = contarDigitos(num)
print(f"O número {num} possui {qntDigitos} dígitos.")
