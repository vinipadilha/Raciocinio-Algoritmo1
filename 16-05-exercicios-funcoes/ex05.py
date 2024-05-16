"""Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais:
taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um
item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas"""

'''taxaImposto: Percentual do imposto sobre vendas'''
'''custo: Custo do item antes do imposto'''

def somaImposto(taxaImposto, custo):
    return custo + (custo * taxaImposto / 100)

taxaImposto = float(input("Digite a taxa de imposto (em %): "))
custo = float(input("Digite o custo do item (antes do imposto): "))

custo_com_imposto = somaImposto(taxaImposto, custo)
print(f"O custo do item incluindo o imposto é: {custo_com_imposto:.2f}")




