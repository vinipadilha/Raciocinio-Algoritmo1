#Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
#e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
#um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
#tempo necessário para que a população do país A ultrapasse a população do país B.

pA = 5000000
pB = 7000000
ano = 0
while True:
    if pA >= pB:
        break
    else:
        pA = (pA * 0.03) + pA
        pB = (pB * 0.02) + pB
        ano += 1

print(f"A população do país A ultrapassou a população do país B em {ano} anos.")

    

