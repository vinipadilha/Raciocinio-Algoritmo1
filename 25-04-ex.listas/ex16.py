"""Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um
total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
receberam salários nos seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
"""
qnt = int(input("Quantos vendedores tem na sua empresa: "))

vendedor = []
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

for i in range(qnt):
    bruto = float(input(f"Qual foi o valor em vendas desta semana do {i + 1}º vendedor: "))
    comissao = float(bruto * 0.09)
    salario = 200 + comissao
    if salario > 200 and salario < 299:
        a += 1
    elif salario > 300 and salario < 399:
        b += 1
    elif salario > 400 and salario < 499:
        c  += 1
    elif salario > 500 and salario < 599:
        d += 1
    elif salario > 600 and salario < 699:
        e += 1
    elif salario > 700 and salario < 799:
        f += 1
    elif salario > 800 and salario < 899:
        g += 1
    elif salario > 900 and salario < 999:
        h += 1
    elif salario > 1000:
        i += 1

print(f"{a} vendedores receberam salario entre R$ 200 e R$ 299")
print(f"{b} vendedores receberam salario entre R$ 300 e R$ 399")
print(f"{c} vendedores receberam salario entre R$ 400 e R$ 499")
print(f"{d} vendedores receberam salario entre R$ 500 e R$ 599")
print(f"{e} vendedores receberam salario entre R$ 600 e R$ 699")
print(f"{f} vendedores receberam salario entre R$ 700 e R$ 799")
print(f"{g} vendedores receberam salario entre R$ 800 e R$ 899")
print(f"{h} vendedores receberam salario entre R$ 900 e R$ 999")
print(f"{i} vendedores receberam salario maior que R$ 1000")
